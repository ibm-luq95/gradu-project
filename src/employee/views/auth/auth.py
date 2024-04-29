# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import FormView


class TechWellLoginView(SuccessMessageMixin, FormView):
    pass
