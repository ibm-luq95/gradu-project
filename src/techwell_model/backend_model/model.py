# -*- coding: utf-8 -*-#
from typing import Optional
from django.utils.translation import gettext as _
from rest_framework.utils.serializer_helpers import ReturnDict

from classification.models import Classification
from classification.serializers.classification import ClassificationSerializer
from core.constants.techwell_model import Q_POSITIVE, Q_NEGATIVE
from core.models.querysets import BaseQuerySetMixin
from core.utils.developments.debugging_print_object import DebuggingPrint
from survey.models import Survey
from techweb_user.models import TechWebUser
from techwell_model.models import ModelQuestion


class TechWellModel:

    ALL_CLASSIFICATIONS = Classification.objects.all()

    def __init__(
        self,
        user: TechWebUser,
        survey_questions: dict[list[dict[str, str, str]]],
        excluded_steps: Optional[list[int]] = None,
    ):
        self._user = user
        self._survey_questions = survey_questions
        self.clean_survey_questions: list[dict[str, str | int]] = []
        self.organized_questions = {f"{Q_POSITIVE}": [], f"{Q_NEGATIVE}": []}
        self.positive_points: list[int] = []
        self.negative_points: list[int] = []
        self.step_1_form: dict = {}

        self.clean_questions(excluded_steps)

    def clean_questions(self, excluded_steps: Optional[list[int]] = None) -> None:
        for key, value in self._survey_questions.items():
            tmp_step_number = int(key[-1])
            if tmp_step_number not in excluded_steps:
                for item in value:
                    tmp_data = {
                        "question": item.get("question"),
                        "answer": item.get("value"),
                    }
                    if item.get("question") in self.negative_questions:
                        self.organized_questions[Q_NEGATIVE].append(tmp_data)
                        tmp_data["question_type"] = Q_NEGATIVE
                        self.negative_points.append(6 - int(item.get("value")))
                    elif item.get("question") in self.positive_questions:
                        self.organized_questions[Q_POSITIVE].append(tmp_data)
                        tmp_data["question_type"] = Q_POSITIVE
                        self.positive_points.append(int(item.get("value")))
                    self.clean_survey_questions.append(tmp_data)
            else:
                DebuggingPrint.pprint("Step one 1 form")
                filtered_dict = next(filter(lambda d: d["name"] == "age", value), None)
                self.step_1_form = {
                    "age": next(filter(lambda d: d["name"] == "age", value), None).get(
                        "value"
                    ),
                    "gender": next(
                        filter(lambda d: d["name"] == "gender", value), None
                    ).get("value"),
                    "department": next(
                        filter(lambda d: d["name"] == "department", value), None
                    ).get("value"),
                    "employment_status": next(
                        filter(lambda d: d["name"] == "employment_status", value), None
                    ).get("value"),
                    "years_of_experience": next(
                        filter(lambda d: d["name"] == "years_of_experience", value), None
                    ).get("value"),
                    "work_environment": next(
                        filter(lambda d: d["name"] == "work_environment", value), None
                    ).get("value"),
                }
                DebuggingPrint.pprint(self.step_1_form)

    @property
    def user(self) -> TechWebUser:
        return self._user

    @user.setter
    def employee_obj(self, user: TechWebUser):
        self._user = user

    @property
    def survey_questions(self) -> dict[list[dict[str, str, str]]]:
        return self._survey_questions

    @survey_questions.setter
    def survey_questions(self, questions: dict[list[dict[str, str, str]]]):
        self._survey_questions = questions

    @property
    def negative_questions(self) -> list[str] | None:
        questions = ModelQuestion.objects.filter(question_type=Q_NEGATIVE).values_list(
            "slug", flat=True
        )
        return list(questions) if questions else None

    @property
    def positive_questions(self) -> list[BaseQuerySetMixin] | None:
        questions = ModelQuestion.objects.filter(question_type=Q_POSITIVE).values_list(
            "slug", flat=True
        )
        return list(questions) if questions else None

    def classify_responses(self) -> ReturnDict:
        """Function to classify responses"""
        # Identifying negative and positive questions based on your description
        # Calculating total score, adjusting for negative questions
        # total_score: int = sum(row[q] for q in TechWellModel.POSITIVE_QUESTIONS) + sum(
        #     6 - row[q] for q in TechWellModel.NEGATIVE_QUESTIONS
        # )

        positive_score = sum(self.positive_points)
        negative_score = sum(self.negative_points)
        total_score = positive_score + negative_score
        DebuggingPrint.pprint(f"total_score -> {total_score}")
        serializer = None
        classified_obj = None
        # Classification based on total score
        for classification in self.ALL_CLASSIFICATIONS:
            if total_score <= classification.min_value:
                DebuggingPrint.pprint(classification)
                classified_obj = classification
                # DebuggingPrint.pprint(classification.get_instance_as_dict)
                DebuggingPrint.rule()
                serializer = ClassificationSerializer(classification)
                break

        survey_obj = Survey()
        survey_obj.user = self.user
        survey_obj.total_score = total_score
        survey_obj.questions_answers = self.organized_questions
        survey_obj.classification = classified_obj
        survey_obj.age = int(self.step_1_form.get("age"))
        survey_obj.department = self.step_1_form.get("department")
        survey_obj.employment_status = self.step_1_form.get("employment_status")
        survey_obj.gender = self.step_1_form.get("gender")
        survey_obj.work_environment = self.step_1_form.get("work_environment")
        survey_obj.years_of_experience = self.step_1_form.get("years_of_experience")
        survey_obj.save()
        return serializer.data
        # if total_score <= 33:
        #     DebuggingPrint.pprint(f"Default: Healthy")
        #     return _("Healthy")
        # elif total_score <= 39:
        #     DebuggingPrint.pprint(f"Default: Mildly Stressed")
        #     return _("Mildly Stressed")
        # elif total_score <= 46:
        #     DebuggingPrint.pprint(f"Default: Highly Stressed")
        #     return _("Highly Stressed")
        # else:
        #     DebuggingPrint.pprint(f"Default: Burned out")
        #     return _("Burned Out")
