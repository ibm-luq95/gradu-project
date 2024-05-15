# -*- coding: utf-8 -*-#
from core.utils.developments.debugging_print_object import DebuggingPrint


class DebuggingLoggingMixin:
    DEBUGGING_ATTRIBUTE_LABEL = "IS_DEBUGGING"

    def debugging_log(self, msg: str) -> None:
        check_attr = getattr(self, DebuggingLoggingMixin.DEBUGGING_ATTRIBUTE_LABEL, None)
        if check_attr is True:
            DebuggingPrint.pprint(msg)
