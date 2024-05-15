# -*- coding: utf-8 -*-#
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from core.choices.survey import (
    SurveyDepartmentsTypeChoices,
    SurveyEmploymentStatusChoices,
    SurveyWorkEnvironmentTypesEnum,
)
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.views.mixins.login_required import TWLoginRequiredMixin
from techwell_model.backend_model.model import TechWellModel
from techwell_model.models import ModelQuestion


class SurveyFormView(TWLoginRequiredMixin, TemplateView):
    template_name = "home/survey_form.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Take your survey".title()))
        step_2_questions = ModelQuestion.objects.filter(step=2)
        step_3_questions = ModelQuestion.objects.filter(step=3)
        step_4_questions = ModelQuestion.objects.filter(step=4)
        step_5_questions = ModelQuestion.objects.filter(step=5)
        context.setdefault("departments_choices", SurveyDepartmentsTypeChoices.choices)
        context.setdefault("employee_status", SurveyEmploymentStatusChoices.choices)
        context.setdefault("work_environments", SurveyWorkEnvironmentTypesEnum.choices)
        context.setdefault("step_2_questions", step_2_questions)
        context.setdefault("step_3_questions", step_3_questions)
        context.setdefault("step_4_questions", step_4_questions)
        context.setdefault("step_5_questions", step_5_questions)
        # kk = TechWellModel(self.request.user)
        # DebuggingPrint.pprint(kk.negative_questions)

        return context
