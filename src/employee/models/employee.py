# -*- coding: utf-8 -*-#
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _

from core.models.mixins.base_model import BaseModelMixin


class Employee(BaseModelMixin):
    user = models.OneToOneField("techweb_user.TechWebUser", on_delete=models.CASCADE)
    employee_id = models.PositiveBigIntegerField(_("ID"))
    token = models.CharField(_("Token"), max_length=255, null=True, blank=True)

    class Meta(BaseModelMixin.Meta):
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
        indexes = [
            models.Index(name="employee_user_idx", fields=["user"]),
            models.Index(name="employee_id_idx", fields=["employee_id"]),
            models.Index(name="employee_token_idx", fields=["token"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["employee_id"],
                name="unique_employee_id_unique_constraint",
                condition=Q(employee_id__isnull=False),
            ),
            models.UniqueConstraint(
                fields=["token"],
                name="unique_employee_token_unique_constraint",
                condition=Q(token__isnull=False),
            ),
        ]
