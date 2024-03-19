# -*- coding: utf-8 -*-#
from core.models.mixins.base_model import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class Recommendations(BaseModelMixin):
    classification = models.ForeignKey(
        to="classification.Classification",
        on_delete=models.CASCADE,
        related_name="recommendations",
    )
    content = models.TextField(_("content"))
