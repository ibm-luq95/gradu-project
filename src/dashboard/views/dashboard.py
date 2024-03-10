# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from django.views.generic import TemplateView


class DashboardLoginView(TemplateView):
    template_name = "dashboard/login.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Manager Login"))

        return context


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Dashboard"))

        return context
