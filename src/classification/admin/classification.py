# -*- coding: utf-8 -*-#
from django.contrib import admin

from classification.models import Classification
from core.admin.base_admin import BaseAdminModelMixin


@admin.register(Classification)
class ClassificationAdmin(BaseAdminModelMixin):
    pass
