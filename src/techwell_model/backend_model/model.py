# -*- coding: utf-8 -*-#
import random
from typing import Optional
from pathlib import PosixPath
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext as _
from rest_framework.exceptions import APIException
from rest_framework.utils.serializer_helpers import ReturnDict
from tabulate import tabulate

from classification.models import Classification
from classification.serializers.classification import ClassificationSerializer
from core.constants.techwell_model import Q_POSITIVE, Q_NEGATIVE
from core.models.querysets import BaseQuerySetMixin
from core.utils.debugging_logging_mixin import DebuggingLoggingMixin
from core.utils.developments.debugging_print_object import DebuggingPrint
from survey.models import Survey
from techweb_user.models import TechWebUser
from techwell_model.helpers.questions_organizer import QuestionsOrganizer
from techwell_model.models import ModelQuestion
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA


class TechWellModel(DebuggingLoggingMixin, QuestionsOrganizer):
    IS_DEBUGGING = True

    ALL_CLASSIFICATIONS = Classification.objects.all()

    def __init__(
        self,
        user: TechWebUser,
        survey_questions: dict[list[dict[str, str, str]]],
        is_debugging: bool = False,
        excluded_steps: Optional[list[int]] = None,
    ):
        self._user = user
        self._dataset: pd.DataFrame = pd.DataFrame()
        self._is_debugging = is_debugging
        self._survey_questions = survey_questions
        self.excluded_steps = excluded_steps
        self.clean_survey_questions: list[dict[str, str | int]] = []
        self.organized_questions = {f"{Q_POSITIVE}": [], f"{Q_NEGATIVE}": []}
        self.positive_points: list[int] = []
        self.negative_points: list[int] = []
        self.step_1_form: dict = {}
        # DebuggingPrint.pprint(self.survey_questions)
        self.load_dataset()
        self.init_dataset()
        self.preprocess_dataset()
        self.init_user_inputs()

    @property
    def survey_questions(self) -> dict[list[dict[str, str, str]]]:
        return self._survey_questions

    @survey_questions.setter
    def survey_questions(self, questions: dict[list[dict[str, str, str]]]):
        self._survey_questions = questions

    @property
    def user(self) -> TechWebUser:
        return self._user

    @user.setter
    def user(self, value: TechWebUser):
        self._user = value

    @property
    def dataset(self) -> pd.DataFrame:
        return self._dataset

    @dataset.setter
    def dataset(self, dataset: pd.DataFrame):
        self._dataset = dataset

    def load_dataset(self) -> None:
        self.debugging_log("Load the data set")
        base_dir = settings.BASE_DIR
        dataset_file: PosixPath = (
            base_dir / "techwell_model" / "backend_model" / "Final_GP_Dataset5.csv"
        )
        if dataset_file.exists() is False:
            raise FileNotFoundError(_("Dataset file not exists!"))
        self.dataset = pd.read_csv(dataset_file.as_posix())

    def init_dataset(self) -> None:
        self.debugging_log("Init Dataset")
        self.dataset.drop(
            [
                "age",
                "Work environment",
                "Gender",
                "Department",
                "employment status",
                "Years of experience",
            ],
            axis=1,
            inplace=True,
        )
        self.dataset.columns = [
            col.replace("{", "")
            .replace("}", "")
            .replace("[", "")
            .replace("]", "")
            .replace(":", "")
            .replace(",", "")
            for col in self.dataset.columns
        ]

    def preprocess_dataset(self) -> None:
        self.debugging_log("Preprocess data")
        # Preprocess data
        label_encoders = {}
        for column in self.dataset.select_dtypes(include=["object"]).columns:
            le = LabelEncoder()
            self.dataset[column] = le.fit_transform(self.dataset[column])
            label_encoders[column] = le
        # Define features and target variable
        self.X = self.dataset.drop("How do you feel?", axis=1)
        self.y = self.dataset["How do you feel?"]

    def init_user_inputs(self) -> pd.DataFrame:
        self.debugging_log("Init user inputs")
        "Init user inputs"
        # self.get_only_survey_question()
        # DebuggingPrint.pprint(self.get_employ_details_only())
        user_inputs = {}
        user_inputs["Unnamed 0"] = random.randint(0, 100)
        for col in self.X.columns:
            slugged_q = slugify(col)
            if slugged_q != "unnamed-0":
                # DebuggingPrint.log(slugged_q)
                q_obj = ModelQuestion.objects.filter(slug=slugged_q)
                if q_obj.exists() is False:
                    raise APIException(_(f"Question {slugged_q} not exists!"))
                q_obj = q_obj.first()
                # user_inputs[col] =
                qq = self.get_answer_value_for_question(q_obj.slug)
                user_inputs[col] = qq.get("value")
        user_df = pd.DataFrame([user_inputs])
        return user_df

    def run_classifier(self):
        self.debugging_log("Run Classifier")
        user_df = self.init_user_inputs()
        # Exclude non-numeric columns from PCA
        numeric_cols = self.X.select_dtypes(include=["number"]).columns
        X_numeric = self.X[numeric_cols]
        user_data_numeric = user_df[numeric_cols]
        # PCA for dimensionality reduction
        pca = PCA(n_components=0.95)
        X_pca = pca.fit_transform(self.X)
        user_data_pca = pca.transform(user_df)
        # Base models
        estimators = [
            ("xgb", XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")),
            ("cat", CatBoostClassifier()),
            ("lgb", LGBMClassifier()),
        ]
        # Stacking model
        stack_model = StackingClassifier(
            estimators=estimators, final_estimator=RandomForestClassifier(random_state=42)
        )
        stack_model.fit(X_pca, self.y)
        y_pred: np.ndarray = stack_model.predict(user_data_pca)
        y_pred_idx = y_pred[0]

        employee_dict = self.get_employ_details_only()
        classification_obj = Classification.objects.filter(
            classification_number=y_pred_idx
        )
        if classification_obj.exists() is False:
            raise APIException(
                _(f"Classification object not found with number {y_pred_idx}")
            )
        classification_obj = classification_obj.first()
        # DebuggingPrint.pprint(classification_obj)
        total_score = self.calc_total_score()
        survey_obj = Survey()
        survey_obj.user = self.user
        survey_obj.questions_answers = self.get_only_survey_question()
        survey_obj.total_score = total_score
        survey_obj.classification = classification_obj
        survey_obj.age = int(employee_dict.get("age"))
        survey_obj.department = employee_dict.get("department")
        survey_obj.employment_status = employee_dict.get("employment_status")
        survey_obj.gender = employee_dict.get("gender")
        survey_obj.work_environment = employee_dict.get("work_environment")
        survey_obj.years_of_experience = employee_dict.get("years_of_experience")
        survey_obj.save()
        serializer = ClassificationSerializer(classification_obj)
        return {
            "prediction_idx": y_pred_idx,
            "data": serializer.data,
            "total_score": total_score,
        }
