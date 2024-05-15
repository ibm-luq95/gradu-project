# -*- coding: utf-8 -*-#
from pathlib import Path
from django.conf import settings
from django.contrib.staticfiles import finders
from django.db import transaction
from django.utils.translation import gettext as _
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File

from classification.data.classification import MAIN_CLASSIFICATIONS
from classification.models import Classification, Recommendations
from core.management.commands.mixins.base_command import BaseCommandMixin
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.utils.developments.prompts import DebuggingPrompt


class Command(BaseCommandMixin):
    help = _("Init techwell backend model classifications into db")

    def handle(self, *args, **options):
        try:
            confirm = DebuggingPrompt.confirm(
                _("Do you want to start init classifications?")
            )
            if confirm is True:
                with transaction.atomic():
                    for classification in MAIN_CLASSIFICATIONS:
                        recommendations = classification.get("recommendations")
                        image_name = classification.get("image_name")
                        all_recommendations_obj: list[Recommendations] = []

                        data = {
                            "label": classification.get("label"),
                            "classification_number": int(
                                classification.get("classification_number")
                            ),
                            "short_advice": classification.get("short_advice"),
                            "conclusion_advice": classification.get("conclusion_advice"),
                            "description": classification.get("description"),
                        }
                        classification_obj = Classification.objects.create(**data)
                        DebuggingPrint.pprint(
                            f"Classification {classification_obj} created successfully!"
                        )
                        DebuggingPrint.pprint(
                            f"Uploading image for {classification_obj}..."
                        )
                        results = finders.find(f"img/base/{image_name}")
                        results_path: Path = Path(results)
                        with results_path.open(mode="rb") as img_file:
                            classification_obj.image = File(
                                img_file, name=results_path.name
                            )
                            classification_obj.save()
                        DebuggingPrint.pprint(f"Creating the recommendations...")
                        for reco in recommendations:
                            reco_obj = Recommendations.objects.create(content=reco)
                            DebuggingPrint.pprint(
                                f"Recommendation {reco_obj} created successfully!"
                            )
                            all_recommendations_obj.append(reco_obj)
                        classification_obj.recommendations.add(*all_recommendations_obj)
                        classification_obj.save()
                        DebuggingPrint.rule()
            else:
                return
        except Exception:
            # self.stdout_output("error", traceback.format_exc())
            DebuggingPrint.print_exception()
