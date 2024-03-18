# -*- coding: utf-8 -*-#
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext as _

from core.models.mixins.base_model import BaseModelMixin


class SurveyAnswers(BaseModelMixin):
    answers = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        null=True,
        help_text=_(
            "Answers input as an array, the correct answer index will set in "
            "correct_answer_index field"
        ),
    )
    question = models.ForeignKey(
        to="survey.SurveyQuestions", on_delete=models.CASCADE, related_name="answers"
    )
    help_text = models.CharField(_("help text"), max_length=200, null=True, blank=True)
    is_optional = models.BooleanField(_("is optional"), default=False)
    correct_answer_index = models.PositiveSmallIntegerField(_("Correct answer index"))

    class Meta(BaseModelMixin.Meta):
        verbose_name = _("Survey Question Answer")
        verbose_name_plural = _("Survey Question Answers")
        indexes = [
            models.Index(name="answer_question_idx", fields=["question"]),
            models.Index(name="answer_is_optional_idx", fields=["is_optional"]),
            models.Index(
                name="answer_correct_answer_idx", fields=["correct_answer_index"]
            ),
        ]
