# -*- coding: utf-8 -*-#
import stringcase
from django.db.models import TextChoices
from django.utils.translation import gettext as _

from core.constants.survey import CST_REMOTE, CST_HYPERD, CST_OFFICE, CST_MALE, CST_FEMALE


class SurveyWorkEnvironmentTypesEnum(TextChoices):
    REMOTE = CST_REMOTE, _(stringcase.sentencecase(CST_REMOTE))
    HYPERD = CST_HYPERD, _(stringcase.sentencecase(CST_HYPERD))
    OFFICE = CST_OFFICE, _(stringcase.sentencecase(CST_OFFICE))


class SurveyGenderTypesEnum(TextChoices):
    MALE = CST_MALE, _(stringcase.sentencecase(CST_MALE))
    FEMALE = CST_FEMALE, _(stringcase.sentencecase(CST_FEMALE))
