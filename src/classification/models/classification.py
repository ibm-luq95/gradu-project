# -*- coding: utf-8 -*-#
from core.models.mixins.base_model import BaseModelMixin
from django.utils.text import slugify
from django.db import models
from django.utils.translation import gettext as _


class Classification(BaseModelMixin):
    slug = models.SlugField(_("Slug"), editable=False, max_length=250)
    label = models.CharField(_("label"), max_length=255)
    description = models.TextField(_("description"), null=True, blank=True)
    min_value = models.PositiveIntegerField(_("min value"), default=0)
    is_enabled = models.BooleanField(_("is_enabled"), default=True)
    short_advice = models.CharField(
        _("short advice"), max_length=250, null=True, blank=True
    )
    conclusion_advice = models.CharField(
        _("conclusion advice"), max_length=250, null=True, blank=True
    )
    image = models.ImageField(
        _("Image"), upload_to="classification_images/", null=True, blank=True
    )
    recommendations = models.ManyToManyField(
        to="classification.Recommendations", related_name="classifications", blank=True
    )

    class Meta(BaseModelMixin.Meta):
        indexes = [
            models.Index(name="classification_label_idx", fields=["label"]),
            models.Index(name="classification_slug_idx", fields=["slug"]),
            models.Index(name="classification_min_value_idx", fields=["min_value"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_slug_classification_cnst",
            ),
        ]

    def __str__(self):
        return f"{self.label} slugged as {self.slug}, Min value: {self.min_value}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(Classification, self).save(*args, **kwargs)
