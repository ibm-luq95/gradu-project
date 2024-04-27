# -*- coding: utf-8 -*-#
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _

from core.models.mixins.base_model import BaseModelMixin


class Employee(BaseModelMixin):
    user = models.OneToOneField("techweb_user.TechWebUser", on_delete=models.CASCADE)

    class Meta(BaseModelMixin.Meta):
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
        indexes = [
            models.Index(name="employee_user_idx", fields=["user"]),
        ]
