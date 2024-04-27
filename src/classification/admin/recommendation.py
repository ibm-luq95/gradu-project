# -*- coding: utf-8 -*-#
from django.contrib import admin

from classification.models import Recommendations
from core.admin.base_admin import BaseAdminModelMixin


@admin.register(Recommendations)
class RecommendationsAdmin(BaseAdminModelMixin):
    list_display = ["content", "get_classification", "created_at"]

    def get_classification(self, obj):
        if hasattr(obj, "classifications"):
            return obj.classifications.get().slug
        else:
            return None
