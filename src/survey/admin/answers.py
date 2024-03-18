# -*- coding: utf-8 -*-#
from django.contrib import admin
from core.admin.base_admin import BaseAdminModelMixin
from survey.models import SurveyAnswers


@admin.register(SurveyAnswers)
class SurveyAnswersAdmin(BaseAdminModelMixin):
    pass
