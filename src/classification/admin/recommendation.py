# -*- coding: utf-8 -*-#
from django.contrib import admin

from classification.models import Recommendations
from core.admin.base_admin import BaseAdminModelMixin


@admin.register(Recommendations)
class RecommendationsAdmin(BaseAdminModelMixin):
    pass
