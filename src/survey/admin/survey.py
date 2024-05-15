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
        "employment_status",
        "created_at",
    ]
    readonly_fields = ["questions_answers", "user", "total_score"]
    search_fields = ["user", "department", "classification", "employment_status"]
