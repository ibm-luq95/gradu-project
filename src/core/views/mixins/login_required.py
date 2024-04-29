# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class TWLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("home:home")
