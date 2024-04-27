# -*- coding: utf-8 -*-#
from core.models.mixins.base_model import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class Recommendations(BaseModelMixin):
    content = models.CharField(_("content"), max_length=250)

    def __str__(self):
        return f"{self.content}"
