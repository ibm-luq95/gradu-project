# -*- coding: utf-8 -*-#
import traceback

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import FormView

from core.utils.developments.debugging_print_object import DebuggingPrint
from techweb_user.forms.login import TWManagerLoginForm
from techweb_user.models import TechWebUser


class TWManagerLoginView(SuccessMessageMixin, FormView):
    template_name = "techweb_user/auth/login.html"
    form_class = TWManagerLoginForm
    success_message: str = _("Login successfully")
    success_url = reverse_lazy("dashboard:home")

    def form_valid(self, form):
        try:
            user_type = form.cleaned_data.get("user_type")
            manager_id = form.cleaned_data.get("manager_id")
            password = form.cleaned_data.get("password")
            fetch_user = TechWebUser.objects.filter(employee_id=manager_id).first()
            if not fetch_user:
                messages.error(self.request, _(f"Manager not found with ID {manager_id}!"))
                return super().form_invalid(form)
            if fetch_user.user_type == "employee":
                messages.error(
                    self.request,
                    _(f"User {manager_id} has problem contact administrator!"),
                )
                return super().form_invalid(form)
            user = authenticate(
                self.request,
                username=form.cleaned_data["manager_id"],
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
        context.setdefault("title", _("Management login"))

        return context
