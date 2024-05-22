# -*- coding: utf-8 -*-#
from django.urls import path, include

from techweb_user.views.logout import TWLogoutView

app_name = "users"

urlpatterns = [
    path("logout/", TWLogoutView.as_view(), name="logout"),
]
