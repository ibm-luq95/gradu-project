# -*- coding: utf-8 -*-#
from core.models.mixins.base_model import BaseModelMixin
from django.utils.text import slugify
from django.db import models
from django.utils.translation import gettext as _


class Classification(BaseModelMixin):
    slug = models.SlugField(_("Slug"), editable=False, max_length=250)
    label = models.CharField(_("label"), max_length=255)
    description = models.TextField(_("description"), null=True, blank=True)
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
    classification_number = models.PositiveSmallIntegerField(
        _("classification_number"), editable=False
    )

    class Meta(BaseModelMixin.Meta):
        indexes = [
            models.Index(name="classification_label_idx", fields=["label"]),
            models.Index(name="classification_slug_idx", fields=["slug"]),
            models.Index(
                name="classification_number_idx", fields=["classification_number"]
            ),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_slug_classification_cnst",
            ),
            models.UniqueConstraint(
                fields=["classification_number"], name="classification_number_unq_cnst"
            ),
        ]

    def __str__(self):
        return (
            f"{self.label} slugged as {self.slug}, Classification number:"
            f" {self.classification_number}"
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(Classification, self).save(*args, **kwargs)
