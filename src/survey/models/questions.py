# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
from django.db import models
from core.models.mixins.base_model import BaseModelMixin


class SurveyQuestions(BaseModelMixin):
    survey = models.ForeignKey(
        to="survey.Survey", on_delete=models.CASCADE, related_name="questions"
    )
    question = models.CharField(_("Question"), max_length=255)
    help_text = models.CharField(_("Help text"), max_length=255, null=True, blank=True)
    is_optional = models.BooleanField(_("is optional"), default=False)

    class Meta(BaseModelMixin.Meta):
        indexes = [
            models.Index(name="question_idx", fields=["question"]),
            models.Index(name="is_optional_idx", fields=["is_optional"]),
        ]
