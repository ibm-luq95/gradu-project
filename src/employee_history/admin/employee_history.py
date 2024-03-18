# -*- coding: utf-8 -*-#
# -*- coding: utf-8 -*-#
from django.contrib import admin
from core.admin.base_admin import BaseAdminModelMixin
from employee_history.models import EmployeeHistory


@admin.register(EmployeeHistory)
class EmployeeHistoryAdmin(BaseAdminModelMixin):
    pass
