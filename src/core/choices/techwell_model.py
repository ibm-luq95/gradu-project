# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
import stringcase
from django.db.models import TextChoices

from core.constants.techwell_model import Q_POSITIVE, Q_NEGATIVE


class QuestionTypesEnum(TextChoices):
    POSITIVE = Q_POSITIVE, _(stringcase.sentencecase(Q_POSITIVE))
    NEGATIVE = Q_NEGATIVE, _(stringcase.sentencecase(Q_NEGATIVE))
