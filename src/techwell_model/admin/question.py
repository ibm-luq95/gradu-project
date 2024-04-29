# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin.base_admin import BaseAdminModelMixin
from techwell_model.models import ModelQuestion


@admin.register(ModelQuestion)
class ModelQuestionAdmin(BaseAdminModelMixin):
    list_display = [
        "question",
        "slug",
        "step",
        "question_type",
        "max_value",
        "min_value",
        "created_at",
    ]
    readonly_fields = ["slug", "created_at", "updated_at"]
