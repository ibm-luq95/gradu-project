# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin.base_admin import BaseAdminModelMixin
from home.models import ContactMessages


@admin.register(ContactMessages)
class ContactMessageAdmin(BaseAdminModelMixin):
    list_display = [
        "email",
        "first_name",
        "last_name",
        "phone",
        "created_at",
    ]
    readonly_fields = ["deleted_at", "created_at", "updated_at"]
