# -*- coding: utf-8 -*-#
from django.urls import path, include

from techweb_user.views import TWLogoutView, TWManagerLoginView

app_name = "auth"

urlpatterns = [
    path("logout/", TWLogoutView.as_view(), name="logout"),
    path("manager/login", TWManagerLoginView.as_view(), name="login"),
]
