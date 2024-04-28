# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin.base_admin import BaseAdminModelMixin
from employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(BaseAdminModelMixin):
    pass
