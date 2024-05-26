# -*- coding: utf-8 -*-#
from django import forms
from django.utils.translation import gettext as _


class TWLoginForm(forms.Form):
    # field_order = ["user_type", "username", "password"]
    # username_field = "email"
    employee_id = forms.CharField(
        label=_("Employee ID"), required=True, widget=forms.NumberInput
    )
    password = forms.CharField(
        label=_("Password"),
        required=True,
        error_messages={"required": _("Password required!")},
        widget=forms.PasswordInput(
            attrs={"class": "input", "autocomplete": "new-password"}
        ),
    )
    remember_me = forms.BooleanField(label=_("Remember me"), required=False)
    agree_terms = forms.BooleanField(
        label=_("Agree to the terms and conditions"), required=True
    )
    user_type = forms.CharField(
        required=False, widget=forms.HiddenInput, initial="employee"
    )


class TWManagerLoginForm(forms.Form):
    manager_id = forms.CharField(
        label=_("Manager ID"), required=True, widget=forms.NumberInput
    )
    password = forms.CharField(
        label=_("Password"),
        required=True,
        error_messages={"required": _("Password required!")},
        widget=forms.PasswordInput(
            attrs={"class": "input", "autocomplete": "new-password"}
        ),
    )
    remember_me = forms.BooleanField(label=_("Remember me"), required=False)
    user_type = forms.CharField(
        required=False, widget=forms.HiddenInput, initial="manager"
    )
