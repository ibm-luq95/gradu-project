# -*- coding: utf-8 -*-#
from core.models.mixins.base_model import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class Classification(BaseModelMixin):
    label = models.CharField(_("label"), max_length=255)
    description = models.TextField(_("description"), null=True, blank=True)
    is_enabled = models.BooleanField(_("is_enabled"), default=True)

    class Meta(BaseModelMixin.Meta):
        indexes = [
            models.Index(name="classification_label_idx", fields=["label"]),
        ]
