# -*- coding: utf-8 -*-#
from django.urls import path, include

from home.views import HomeView, ContactView, ContactAPIView

app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", ContactView.as_view(), name="contact"),
    path("contact/api", ContactAPIView.as_view(), name="contact_api"),
]
