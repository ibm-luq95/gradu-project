# -*- coding: utf-8 -*-#
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from techwell_model.models import ModelQuestion


class SurveyView(TemplateView):
    template_name = "home/survey.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("take survey".title()))

        return context


class SurveyFormView(TemplateView):
    template_name = "home/survey_form.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("survey form".title()))
        step_2_questions = ModelQuestion.objects.filter(step=2)
        step_3_questions = ModelQuestion.objects.filter(step=3)
        step_4_questions = ModelQuestion.objects.filter(step=4)
        step_5_questions = ModelQuestion.objects.filter(step=5)
        context.setdefault("step_2_questions", step_2_questions)
        context.setdefault("step_3_questions", step_3_questions)
        context.setdefault("step_4_questions", step_4_questions)
        context.setdefault("step_5_questions", step_5_questions)

        return context
