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
from home.models import ContactMessages
from survey.models import Survey
from techweb_user.models import TechWebUser


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
