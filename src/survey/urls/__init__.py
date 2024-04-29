# -*- coding: utf-8 -*-#
from django.urls import path, include

from survey.views import SurveyFormView, SurveyAPIView

app_name = "survey"

urlpatterns = [
    path("form", SurveyFormView.as_view(), name="survey_form"),
    path("api/", SurveyAPIView.as_view(), name="api")
]
