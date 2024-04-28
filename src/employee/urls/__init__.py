# -*- coding: utf-8 -*-#
from django.urls import path, include

from employee.views.auth import TWLogoutView

app_name = "employee"

urlpatterns = [
    path("logout", TWLogoutView.as_view(), name="logout"),
    # path("create", "", name="create"),
]
