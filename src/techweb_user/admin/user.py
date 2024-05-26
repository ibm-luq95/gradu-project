# -*- coding: utf-8 -*-#
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from core.admin.base_admin import BaseAdminModelMixin
from techweb_user.models import TechWebUser


@admin.register(TechWebUser)
class TechWellUserAdmin(UserAdmin):
    ordering = ("employee_id",)
    list_display = [
        "employee_id",
        "email",
        "first_name",
        "last_name",
        "user_type",
        "created_at",
    ]
    readonly_fields = ["deleted_at", "created_at", "updated_at", "last_login"]
    list_filter = ["user_type", "status"]
    fieldsets = (
        (None, {"fields": ("employee_id", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "employee_id",
                    "first_name",
                    "last_name",
                    "email",
                    "user_type",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
