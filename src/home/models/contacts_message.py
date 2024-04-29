# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
from django.db import models

from core.models.mixins.base_model import BaseModelMixin


class ContactMessages(BaseModelMixin):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(_("email address"), max_length=100)
    phone = models.CharField(_("phone number"), max_length=50, null=True, blank=True)
    message = models.TextField(_("message"))

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name}"
