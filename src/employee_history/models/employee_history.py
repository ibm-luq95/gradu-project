# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
from django.db import models

from core.models.mixins.base_model import BaseModelMixin


class EmployeeHistory(BaseModelMixin):
    employee = models.ForeignKey(
        to="employee.Employee", on_delete=models.CASCADE, related_name="history"
    )
    history_created_date = models.DateTimeField(_("history created date"))

    class Meta(BaseModelMixin.Meta):
        verbose_name = _("Employee History")
        verbose_name_plural = _("Employee Histories")
        indexes = [
            models.Index(name="employee_history_employee_idx", fields=["employee"]),
        ]
