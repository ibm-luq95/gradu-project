# -*- coding: utf-8 -*-#
import traceback

from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from core.utils.developments.debugging_print_object import DebuggingPrint
from employee.forms.auth import TWLoginForm


class HomeView(SuccessMessageMixin, FormView):
    template_name = "home/home.html"
    form_class = TWLoginForm
    success_message: str = _("Login successfully")
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        try:
            if form.cleaned_data.get("agree_terms") is False:
                form.add_error(
                    "agree_terms", _("You must agree with the terms and conditions!")
                )
                return super().form_invalid(form)
            user = authenticate(
                self.request,
                username=form.cleaned_data["employee_id"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(self.request, user)
            else:
                messages.error(self.request, _("User credentials not correct!"))
                return super().form_invalid(form)
            return super().form_valid(form)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
            messages.error(self.request, _("Error while login"))
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("TechWell"))

        return context
