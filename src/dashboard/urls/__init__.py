# -*- coding: utf-8 -*-#
from django.urls import path, include

from dashboard.views import DashboardLoginView, DashboardView, DashboardAPIView

app_name = "dashboard"

urlpatterns = [
    path("login", DashboardLoginView.as_view(), name="login"),
    path("dashboard", DashboardView.as_view(), name="home"),
    path("api/", DashboardAPIView.as_view(), name="api"),
]
