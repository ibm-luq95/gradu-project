# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

from core.choices.techwell_model import QuestionTypesEnum
from core.models.mixins.base_model import BaseModelMixin


class ModelQuestion(BaseModelMixin):
    question_type = models.CharField(
        _("Type"), max_length=20, choices=QuestionTypesEnum.choices
    )
    question = models.CharField(_("Question"), max_length=250)
    slug = models.SlugField(_("Slug"), editable=False, max_length=250)
    max_value = models.PositiveSmallIntegerField(_("Max value"), default=5)
    min_value = models.PositiveSmallIntegerField(_("Min value"), default=1)
    max_value_help_text = models.CharField(
        _("Max help text"), max_length=250, null=True, blank=True
    )
    min_value_help_text = models.CharField(
        _("Min help text"), max_length=250, null=True, blank=True
    )
    step = models.PositiveSmallIntegerField(_("Step number"), default=0)

    class Meta(BaseModelMixin.Meta):
        ordering = ["question"]
        indexes = [
            models.Index(name="model_qut_type_idx", fields=["question_type"]),
            models.Index(name="model_qut_slug_idx", fields=["slug"]),
            models.Index(name="model_qut_step_idx", fields=["step"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["slug"],
                name="unique_slug_model_question_cnst",
            ),
        ]

    class Meta(BaseModelMixin.Meta):
        ordering = ["step"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(ModelQuestion, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.question} slugged as {self.slug}"
