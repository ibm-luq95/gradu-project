# -*- coding: utf-8 -*-#
from django.contrib import admin
from core.admin.base_admin import BaseAdminModelMixin
from survey.models import Survey


@admin.register(Survey)
class SurveyAdmin(BaseAdminModelMixin):
    list_display = [
        "user",
        "age",
        "department",
        "classification",
        "total_score",
        "created_at",
    ]
    readonly_fields = ["questions_answers", "user", "total_score"]
