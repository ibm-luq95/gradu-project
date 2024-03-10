# -*- coding: utf-8 -*-#
from django.urls import path, include

from home.views import HomeView, ContactView, SurveyView, SurveyFormView

app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", ContactView.as_view(), name="contact"),
    path("survey", SurveyView.as_view(), name="survey"),
    path("survey/form", SurveyFormView.as_view(), name="survey_form"),
]
