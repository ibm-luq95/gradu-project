# -*- coding: utf-8 -*-#
from rest_framework.exceptions import APIException

from core.utils.developments.debugging_print_object import DebuggingPrint
from techwell_model.models import ModelQuestion


class QuestionsOrganizer:

    def get_only_survey_question(self):
        user_inputs = {}
        for step_no, questions in self.survey_questions.items():
            step_id = int(step_no[-1])
            if step_id not in self.excluded_steps:
                # DebuggingPrint.print(step_id, questions)
                for q in questions:
                    q_obj = ModelQuestion.objects.filter(slug=q.get("question"))
                    if q_obj.exists() is True:
                        q_obj = q_obj.first()
                    else:
                        raise APIException(detail=_(f"Question {q} not exists!"))
                    user_inputs[q_obj.question] = q.get("value")
        DebuggingPrint.pprint(user_inputs)
        return user_inputs

    def get_employ_details_only(self) -> dict:
        item = self.survey_questions.get("step1")
        data = {}
        for i in item:
            data[i.get("name")] = i.get("value")
        return data

    def get_answer_value_for_question(self, question_slug: str) -> dict[str, str, str]:
        for step_no, questions in self.survey_questions.items():
            for q in questions:
                if q.get("question") == question_slug:
                    return q

    def calc_total_score(self) -> int:
        survey_inputs = self.get_only_survey_question()
        answers_list = []
        for question, value in survey_inputs.items():
            answers_list.append(int(value))

        return sum(answers_list)
