# -*- coding: utf-8 -*-#
from django.contrib import admin
from core.admin.base_admin import BaseAdminModelMixin
from survey.models import SurveyQuestions


@admin.register(SurveyQuestions)
class SurveyQuestionsAdmin(BaseAdminModelMixin):
    pass
