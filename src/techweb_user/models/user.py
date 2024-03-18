# -*- coding: utf-8 -*-#
from django.urls import reverse_lazy

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from core.choices.techweb_user import TechWebUserTypeChoices, TechWebUserStatusChoices
from core.models.mixins.base_model import BaseModelMixin
from .manager import TechWebUserManager


class TechWebUser(BaseModelMixin, AbstractBaseUser, PermissionsMixin):
    """TechWebUser, it used instead of default django user model

    Args:
        BaseModelMixin (_type_): _description_
        AbstractBaseUser (_type_): _description_
        PermissionsMixin (_type_): _description_

    Returns:
        _type_: _description_
    """

    first_name = models.CharField(_("first name"), max_length=15)
    last_name = models.CharField(_("last name"), max_length=15)
    email = models.EmailField(_("email address"))
    is_staff = models.BooleanField(_("is staff"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    user_type = models.CharField(
        _("user type"), choices=TechWebUserTypeChoices.choices, max_length=15
    )
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=TechWebUserStatusChoices.choices,
        default=TechWebUserStatusChoices.ENABLED,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_type"]

    objects = TechWebUserManager()

    class Meta:
        verbose_name = _("TechWeb User")
        verbose_name_plural = _("TechWeb Users")
        ordering = ["-created_at", "-updated_at"]
        indexes = [
            models.Index(name="user_email_idx", fields=["email"]),
            models.Index(name="user_type_idx", fields=["user_type"]),
            models.Index(name="user_status_idx", fields=["status"]),
            models.Index(name="user_is_active_idx", fields=["is_active"]),
            models.Index(name="user_is_staff_idx", fields=["is_staff"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["email"], name="unique_user_email_unique_constraint"
            )
        ]
        # permissions = [("developer_user", "Developer User")]

    def __str__(self):
        full_info = self.fullname
        if full_info != "":
            return _(f"User - {full_info}")
        else:
            return _(f"User - {self.email}")

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super(TechWebUser, self).save(*args, **kwargs)
