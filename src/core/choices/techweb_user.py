# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
import stringcase
from django.db.models import TextChoices

from core.constants.status import (
    CON_REJECTED,
    CON_ARCHIVED,
    CON_DISABLED,
    CON_CANCELED,
    CON_PENDING,
    CON_ENABLED,
)
from core.constants.techweb_user import (
    CON_TUSER_EMPLOYEE,
    CON_TUSER_MANAGER,
    CON_TUSER_BOTH,
)


class TechWebUserTypeChoices(TextChoices):
    EMPLOYEE = CON_TUSER_EMPLOYEE, _(stringcase.sentencecase(CON_TUSER_EMPLOYEE))
    MANAGER = CON_TUSER_MANAGER, _(stringcase.sentencecase(CON_TUSER_MANAGER))
    BOTH = CON_TUSER_BOTH, _(stringcase.sentencecase(CON_TUSER_BOTH))


class TechWebUserStatusChoices(TextChoices):
    ENABLED = CON_ENABLED, _(stringcase.sentencecase(CON_ENABLED))
    PENDING = CON_PENDING, _(stringcase.sentencecase(CON_PENDING))
    CANCELED = CON_CANCELED, _(stringcase.sentencecase(CON_CANCELED))
    DISABLED = CON_DISABLED, _(stringcase.sentencecase(CON_DISABLED))
    ARCHIVED = CON_ARCHIVED, _(stringcase.sentencecase(CON_ARCHIVED))
    REJECTED = CON_REJECTED, _(stringcase.sentencecase(CON_REJECTED))
