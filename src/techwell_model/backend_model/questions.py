# -*- coding: utf-8 -*-#
from typing import Union

from django.utils.translation import gettext as _

QUESTIONS: dict[str, list[dict[str, Union[str, int, dict[str, str]]]]] = {
    "positive": [
        {
            "question": _("Do you often feel overwhelmed by your workload?"),
            "max_value": 5,
            "min_value": 1,
            "step": 2,
            "help_text": {
                "max": _("Extremely overwhelmed"),
                "min": _("Not at all overwhelmed"),
            },
        },
        {
            "question": _("Do you frequently work beyond your scheduled hours?"),
            "max_value": 5,
            "min_value": 1,
            "step": 2,
            "help_text": {
                "max": _("Extremely frequently"),
                "min": _("Not at all frequently"),
            },
        },
        {
            "question": _("Do you often feel isolated when dealing with work challenges?"),
            "max_value": 5,
            "min_value": 1,
            "step": 3,
            "help_text": {
                "max": _("Extremely isolated"),
                "min": _("Not at all isolated"),
            },
        },
        {
            "question": _("Do you frequently think about work in your personal time?"),
            "max_value": 5,
            "min_value": 1,
            "step": 4,
            "help_text": {
                "max": _("Extremely"),
                "min": _("Not at all"),
            },
        },
        {
            "question": _("Does your work often interfere with personal or family time?"),
            "max_value": 5,
            "min_value": 1,
            "step": 4,
            "help_text": {
                "max": _("Extremely interfere"),
                "min": _("Not at all"),
            },
        },
        {
            "question": _("Do you regularly feel physically or emotionally exhausted?"),
            "max_value": 5,
            "min_value": 1,
            "step": 5,
            "help_text": {
                "max": _("Extremely exhausted"),
                "min": _("Not at all exhausted"),
            },
        },
        {
            "question": _(
                "Do you experience symptoms like sleep issues, anxiety, or low mood?"
            ),
            "max_value": 5,
            "min_value": 1,
            "step": 5,
            "help_text": {
                "max": _("Extremely"),
                "min": _("Not at all"),
            },
        },
    ],
    "negative": [
        {
            "question": _("Is your workload generally manageable?"),
            "max_value": 5,
            "min_value": 1,
            "step": 2,
            "help_text": {
                "max": _("Extremely manageable"),
                "min": _("Not at all manageable"),
            },
        },
        {
            "question": _("Do you feel supported by your manager and team?"),
            "max_value": 5,
            "min_value": 1,
            "step": 3,
            "help_text": {
                "max": _("Extremely supported"),
                "min": _("Not at all supported"),
            },
        },
        {
            "question": _(
                "Are you satisfied with the resources and help available at work?"
            ),
            "max_value": 5,
            "min_value": 1,
            "step": 3,
            "help_text": {
                "max": _("Extremely satisfied"),
                "min": _("Not at all satisfied"),
            },
        },
        {
            "question": _("Do you feel you have a healthy work-life balance?"),
            "max_value": 5,
            "min_value": 1,
            "step": 4,
            "help_text": {
                "max": _("Extremely healthy"),
                "min": _("Not at all healthy"),
            },
        },
        {
            "question": _("Do you regularly engage in physical or leisure activities?"),
            "max_value": 5,
            "min_value": 1,
            "step": 5,
            "help_text": {
                "max": _("Extremely engage"),
                "min": _("Not at all engage"),
            },
        },
    ],
}

__all__ = ["QUESTIONS"]
