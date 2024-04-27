# -*- coding: utf-8 -*-#
from django.contrib import admin

from classification.models import Classification
from core.admin.base_admin import BaseAdminModelMixin


@admin.register(Classification)
class ClassificationAdmin(BaseAdminModelMixin):
    list_display = ["label", "slug", "min_value", "image", "is_enabled", "created_at"]
    list_filter = ["label", "slug", "min_value", "is_enabled", "created_at"]
    search_fields = ["label", "slug", "min_value"]
