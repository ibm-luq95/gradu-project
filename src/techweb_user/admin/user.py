# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin.base_admin import BaseAdminModelMixin
from techweb_user.models import TechWebUser


@admin.register(TechWebUser)
class TechWellUserAdmin(BaseAdminModelMixin):
    list_display = [
        "employee_id",
        "token",
        "email",
        "first_name",
        "last_name",
        "user_type",
        "created_at",
    ]
    readonly_fields = ["deleted_at", "created_at", "updated_at"]
