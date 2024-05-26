# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "users"

urlpatterns = [
    path("auth/", include("techweb_user.urls.auth"), name="auth"),
]
