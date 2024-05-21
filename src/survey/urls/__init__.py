# -*- coding: utf-8 -*-#
from django.urls import path

from survey.views import (
    SurveyFormView,
    SurveyAPIView,
    EmployeeSurveyListView,
    EmployeeSurveyDetailView,
)

app_name = "survey"

urlpatterns = [
    path("form", SurveyFormView.as_view(), name="survey_form"),
    path("list", EmployeeSurveyListView.as_view(), name="list"),
    path("details/<uuid:pk>", EmployeeSurveyDetailView.as_view(), name="details"),
    path("api/", SurveyAPIView.as_view(), name="api"),
]
