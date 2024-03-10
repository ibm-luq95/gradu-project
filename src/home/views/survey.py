# -*- coding: utf-8 -*-#
from django.views.generic import TemplateView
from django.utils.translation import gettext as _


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

        return context
