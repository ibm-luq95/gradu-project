# -*- coding: utf-8 -*-#
from django import forms
from django.utils.translation import gettext as _


class ContactForm(forms.Form):
    first_name = forms.CharField(label=_("First name"), required=True)
    last_name = forms.CharField(label=_("Last name"), required=True)
    email = forms.EmailField(label=_("Email address"), required=True)
    phone = forms.CharField(label=_("Phone number"), required=False)
    details = forms.CharField(label=_("Details"), widget=forms.Textarea, required=True)
