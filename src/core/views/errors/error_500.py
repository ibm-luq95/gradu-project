# -*- coding: utf-8 -*-#
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext as _


def custom_500(request):
    return render(request, "errors/500.html", status=500)


class CustomErrorPage(TemplateView):
    template_name = "errors/500.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Error!"))
        context.setdefault("error_msg", _("Error please contact administrator!"))
        return context
