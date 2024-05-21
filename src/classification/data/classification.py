# -*- coding: utf-8 -*-#
from typing import List, Tuple, Union

from django.utils.translation import gettext as _

MAIN_CLASSIFICATIONS: List[dict[str, Union[str, int, Tuple[str], List[str]]]] = [
    {
        "label": _("Healthy"),
        "image_name": "Healthy.jpg",
        "min_value": 33,
        "classification_number": 2,
        "description": _(
            "Feeling generally positive and capable of handling daily stressors"
            " effectively."
        ),
        "short_advice": _(
            "Congratulations on maintaining a good balance! To continue thriving"
        ),
        "conclusion_advice": _("Remember, to always stay connected!"),
        "recommendations": (
            _("Remember the importance of regular breaks, even on busy days."),
            _(
                "Engaging in activities outside of work, whether it's a hobby or exercise,"
                " can further enhance your mental resilience."
            ),
            _(
                "Stay connected with your support network and don't hesitate to seek help"
                " if you ever feel overwhelmed."
            ),
        ),
    },
    {
        "label": _("Mildly Stressed"),
        "image_name": "Mildly Stressed.png",
        "min_value": 39,
        "classification_number": 4,
        "conclusion_advice": _("Remember, stay safe."),
        "description": _(
            "Coping well but occasionally feel overwhelmed or anxious due to manageable"
            " stressors in your life."
        ),
        "short_advice": _(
            "It's great that you're managing well overall, but there are signs of stress"
            " to address."
        ),
        "recommendations": (
            _(
                "Consider refining your work-life balance; perhaps delegating tasks or"
                " setting more realistic deadlines could help"
            ),
            _(
                "Mindfulness techniques, like meditation or deep breathing exercises, can"
                " be highly effective."
            ),
            _(
                "Also, ensure you're getting adequate rest and using your time off to"
                " truly disconnect and recharge."
            ),
        ),
    },
    {
        "label": _("Highly Stressed"),
        "min_value": 46,
        "classification_number": 3,
        "image_name": "Highly Stressed.webp",
        "short_advice": _(
            "Your well-being is crucial, and it's important to take steps to reduce your"
            " stress levels."
        ),
        "description": _("Feeling overwhelmed, drained, and unable to cope."),
        "conclusion_advice": _("Remember, we are always here when you need us!"),
        "recommendations": (
            _("Prioritize tasks and discuss workload management with your supervisor."),
            _(
                "Regular physical activity and a healthy diet can significantly impact"
                " your stress levels."
            ),
            _(
                "It might also be beneficial to explore stress management resources or"
                " speak with a mental health professional for personalized strategies."
            ),
        ),
    },
    {
        "label": _("Burned Out"),
        "image_name": "BurnOut.png",
        "classification_number": 1,
        "min_value": 50,
        "short_advice": _(
            "We understand you're experiencing burnout, and I want to offer some concise"
            " advice."
        ),
        "description": _(
            "Experiencing extreme mental and physical exhaustion,  feeling detached, and"
            " lacking motivation, typically due to prolonged stress."
        ),
        "recommendations": (
            _("Please consider taking a well-deserved break to rest and recharge."),
            _(
                "It's important to set clear boundaries around your work hours and"
                " prioritize self-care, including adequate sleep, exercise, and healthy"
                " eating."
            ),
            _(
                "Don't hesitate to seek support from management, HR, or a mental health"
                " professional."
            ),
        ),
        "conclusion_advice": _("Remember, your well-being is paramount."),
    },
]

MAIN_CLASSIFICATIONS_LBL_ONLY = tuple([
    classification["label"] for classification in MAIN_CLASSIFICATIONS
])
