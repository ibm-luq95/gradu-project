# -*- coding: utf-8 -*-#
import traceback
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, FormView
from django.contrib import messages

from core.choices.survey import SurveyDepartmentsTypeChoices
from core.constants.techweb_user import (
    CON_TUSER_EMPLOYEE,
    CON_TUSER_BOTH,
    CON_TUSER_MANAGER,
)
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.views.mixins.login_required import TWLoginRequiredMixin
from employee.forms.auth import TWManagerLoginForm
from home.models import ContactMessages
from survey.models import Survey
from techweb_user.models import TechWebUser


class DashboardLoginView(SuccessMessageMixin, FormView):
    template_name = "dashboard/login.html"
    form_class = TWManagerLoginForm
    success_message = _("Manager login successfully")
    success_url = reverse_lazy("dashboard:home")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Manager Login"))

        return context

    def form_valid(self, form):
        try:
            token = form.cleaned_data.get("token")
            employee_id = form.cleaned_data.get("employee_id")
            password = form.cleaned_data.get("password")
            if not employee_id:
                form.add_error("employee_id", _("Employee ID required!"))
                messages.error(self.request, _("Employee ID required!"))
                return super().form_invalid(form)
            if not token:
                form.add_error("token", _("Token required!"))
                messages.error(self.request, _("Token required!"))
                return super().form_invalid(form)
            if not password:
                form.add_error("password", _("Password required!"))
                messages.error(self.request, _("Password required!"))
                return super().form_invalid(form)
            if form.cleaned_data.get("agree_terms") is False:
                messages.error(
                    self.request, _("You must agree with the terms and conditions!!")
                )
                form.add_error(
                    "agree_terms", _("You must agree with the terms and conditions!")
                )
                return super().form_invalid(form)
            user = TechWebUser.objects.filter(employee_id=employee_id).first()
            if user is None:
                messages.error(self.request, _("User credentials not correct!"))
                form.add_error("employee_id", _("User credentials not correct!"))
                return super().form_invalid(form)
            if user.user_type == CON_TUSER_EMPLOYEE:
                messages.error(self.request, _("Not allowed to login!"))
                form.add_error("employee_id", _("Not allowed to login!"))
                return super().form_invalid(form)
            if user.token != token:
                messages.error(self.request, _("User token not correct!"))
                form.add_error("token", _("User token not correct!"))
                return super().form_invalid(form)
            check = authenticate(
                self.request,
                username=employee_id,
                password=password,
            )
            if user is not None:
                login(self.request, check)
            else:
                messages.error(self.request, _("User credentials not correct!"))
                return super().form_invalid(form)
            return super().form_valid(form)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
            messages.error(self.request, _("Error while login"))
            return super().form_invalid(form)


class DashboardView(TWLoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def test_func(self) -> bool:
        user = self.request.user
        return user.user_type == CON_TUSER_MANAGER or user.user_type == CON_TUSER_BOTH

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Dashboard"))

        total_employees = TechWebUser.objects.all().count()
        context.setdefault("total_employees", total_employees)
        total_surveys = Survey.objects.count()
        context.setdefault("total_surveys", total_surveys)
        total_contact_messages = ContactMessages.objects.count()
        context.setdefault("total_contact_messages", total_contact_messages)

        return context
