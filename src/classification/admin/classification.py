# -*- coding: utf-8 -*-#
from django.contrib import admin

from classification.models import Classification
from core.admin.base_admin import BaseAdminModelMixin


@admin.register(Classification)
class ClassificationAdmin(BaseAdminModelMixin):
    list_display = [
        "label",
        "slug",
        "min_value",
        "image",
        "get_total_survey",
        "total_recommendations",
        "is_enabled",
        "created_at",
    ]
    list_filter = ["label", "slug", "min_value", "is_enabled", "created_at"]
    search_fields = ["label", "slug", "min_value"]

    def get_total_survey(self, obj: Classification) -> int:
        if hasattr(obj, "surveys"):
            return obj.surveys.count()
        else:
            return 0

    def total_recommendations(self, obj: Classification) -> int:
        if hasattr(obj, "recommendations"):
            return obj.recommendations.count()
        else:
            return 0
