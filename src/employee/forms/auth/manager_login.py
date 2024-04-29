# -*- coding: utf-8 -*-#
from django import forms
from django.utils.translation import gettext as _

from employee.forms.auth import TWLoginForm


class TWManagerLoginForm(TWLoginForm):
    # field_order = ["user_type", "username", "password"]
    # username_field = "email"
    token = forms.CharField(label=_("Token"), required=True)
