# -*- coding: utf-8 -*-#
import stringcase
from django.db.models import TextChoices
from django.utils.translation import gettext as _

from core.constants.survey import (
    CST_REMOTE,
    CST_HYPERD,
    CST_OFFICE,
    CST_MALE,
    CST_FEMALE,
    CLSF_SOFTWARE_DEVELOPMENT,
    CLSF_HARDWARE_DEVELOPMENT,
    CLSF_IT_SERVICES,
    CLSF_CYBER_SECURITY,
    CLSF_OTHER,
    EMP_STATUS_FULL_TIME,
    EMP_STATUS_PART_TIME,
    EMP_STATUS_CONTRACT,
)


class SurveyWorkEnvironmentTypesEnum(TextChoices):
    REMOTE = CST_REMOTE, _(stringcase.sentencecase(CST_REMOTE))
    HYPERD = CST_HYPERD, _(stringcase.sentencecase(CST_HYPERD))
    OFFICE = CST_OFFICE, _(stringcase.sentencecase(CST_OFFICE))


class SurveyGenderTypesEnum(TextChoices):
    MALE = CST_MALE, _(stringcase.sentencecase(CST_MALE))
    FEMALE = CST_FEMALE, _(stringcase.sentencecase(CST_FEMALE))


class SurveyDepartmentsTypeChoices(TextChoices):
    SOFTWARE_DEVELOPMENT = CLSF_SOFTWARE_DEVELOPMENT, _(
        stringcase.sentencecase(CLSF_SOFTWARE_DEVELOPMENT)
    )
    HARDWARE_DEVELOPMENT = CLSF_HARDWARE_DEVELOPMENT, _(
        stringcase.sentencecase(CLSF_HARDWARE_DEVELOPMENT)
    )
    CYBER_SECURITY = CLSF_CYBER_SECURITY, _(stringcase.sentencecase(CLSF_CYBER_SECURITY))
    IT_SERVICES = CLSF_IT_SERVICES, _(stringcase.sentencecase(CLSF_IT_SERVICES))
    OTHER = CLSF_OTHER, _(stringcase.sentencecase(CLSF_OTHER))


class SurveyEmploymentStatusChoices(TextChoices):
    FULL_TIME = EMP_STATUS_FULL_TIME, _(stringcase.sentencecase(EMP_STATUS_FULL_TIME))
    PART_TIME = EMP_STATUS_PART_TIME, _(stringcase.sentencecase(EMP_STATUS_PART_TIME))
    CONTRACT = EMP_STATUS_CONTRACT, _(stringcase.sentencecase(EMP_STATUS_CONTRACT))
