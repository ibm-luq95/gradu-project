# -*- coding: utf-8 -*-#
from core.constants.css_classes import (
    TW_INPUTS_CLASS,
    TW_LOGIN_CHECKBOX_INPUT,
    TW_LOGIN_TEXT_INPUT,
)


def css_constants(request) -> dict:
    return {
        "TW_INPUTS_CLASS": TW_INPUTS_CLASS,
        "TW_LOGIN_TEXT_INPUT": TW_LOGIN_TEXT_INPUT,
        "TW_LOGIN_CHECKBOX_INPUT": TW_LOGIN_CHECKBOX_INPUT,
    }
