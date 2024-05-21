# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices.survey import (
    SurveyWorkEnvironmentTypesEnum,
    SurveyGenderTypesEnum,
    SurveyDepartmentsTypeChoices,
    SurveyEmploymentStatusChoices,
)
from core.models.mixins.base_model import BaseModelMixin
from techweb_user.models import TechWebUser


class Survey(BaseModelMixin):
    user = models.ForeignKey(
        to=TechWebUser, on_delete=models.CASCADE, related_name="surveys"
    )
    total_score = models.PositiveSmallIntegerField(_("Total score"))
    classification = models.ForeignKey(
        to="classification.Classification",
        on_delete=models.CASCADE,
        related_name="surveys",
    )
    questions_answers = models.JSONField(_("Questions answers"), editable=False)
    age = models.PositiveSmallIntegerField(_("Age"))
    gender = models.CharField(
        _("Gender"), max_length=10, choices=SurveyGenderTypesEnum.choices
    )
    department = models.CharField(
        _("Department"), max_length=50, choices=SurveyDepartmentsTypeChoices.choices
    )
    employment_status = models.CharField(
        _("Employment Status"),
        max_length=100,
        choices=SurveyEmploymentStatusChoices.choices,
    )
    years_of_experience = models.CharField(_("years of experience"), max_length=20)
    work_environment = models.CharField(
        _("work environment"),
        max_length=20,
        choices=SurveyWorkEnvironmentTypesEnum.choices,
    )

    class Meta(BaseModelMixin.Meta):
        verbose_name = _("Survey")
        verbose_name_plural = _("Surveys")
        indexes = [
            models.Index(name="department_idx", fields=["department"]),
            models.Index(name="employment_status_idx", fields=["employment_status"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return _(f"Survey for {self.user} - {self.classification} - {self.total_score}")

    @property
    def name(self) -> str:
        return _(f"Survey at {self.created_at.date()}")
