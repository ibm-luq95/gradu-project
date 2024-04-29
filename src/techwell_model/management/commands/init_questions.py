# -*- coding: utf-8 -*-#
import traceback

from core.management.commands.mixins.base_command import BaseCommandMixin
from django.utils.translation import gettext as _
from django.db import transaction

from core.utils.developments.debugging_print_object import DebuggingPrint
from core.utils.developments.prompts import DebuggingPrompt
from techwell_model.backend_model.questions import QUESTIONS
from techwell_model.models import ModelQuestion


class Command(BaseCommandMixin):
    help = _("Init positive and negative questions into db")

    def handle(self, *args, **options):
        try:
            confirm = DebuggingPrompt.confirm(
                _("Do you want to start init positive & negative questions?")
            )
            if confirm is True:
                with transaction.atomic():
                    for q_type, questions in QUESTIONS.items():
                        # DebuggingPrint.rule(q_type)
                        # DebuggingPrint.log(questions)
                        for q in questions:
                            data = {
                                "question_type": q_type,
                                "question": q.get("question").strip(),
                                "max_value": q.get("max_value"),
                                "min_value": q.get("min_value"),
                                "step": q.get("step"),
                                "max_value_help_text": q.get("help_text")
                                .get("max")
                                .strip(),
                                "min_value_help_text": q.get("help_text")
                                .get("min")
                                .strip(),
                            }
                            m_qs = ModelQuestion.objects.create(**data)
                            DebuggingPrint.pprint(f"Question {m_qs} saved")
                    DebuggingPrint.log("Questions created successfully!")
            else:
                return
        except Exception:
            # self.stdout_output("error", traceback.format_exc())
            DebuggingPrint.print_exception()
