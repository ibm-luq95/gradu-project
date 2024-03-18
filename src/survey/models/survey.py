# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.models.mixins.base_model import BaseModelMixin


class Survey(BaseModelMixin):
    title = models.CharField(_("Title"), max_length=100)
    is_active = models.BooleanField(_("is active"), default=True)
    summary = models.TextField(_("Summary"), null=True, blank=True)

    class Meta(BaseModelMixin.Meta):
        verbose_name = _("Survey")
        verbose_name_plural = _("Surveys")
        indexes = [
            models.Index(name="survey_title_idx", fields=["title"]),
            models.Index(name="survey_is_active_idx", fields=["is_active"]),
        ]
