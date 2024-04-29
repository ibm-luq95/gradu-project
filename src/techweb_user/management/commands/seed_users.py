# -*- coding: utf-8 -*-#
from faker import Faker

from core.choices.techweb_user import TechWebUserTypeChoices
from core.management.commands.mixins.base_command import BaseCommandMixin
from django.utils.translation import gettext as _
from django.db import transaction
import random
import secrets
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.utils.developments.prompts import DebuggingPrompt
from techwell_model.backend_model.questions import QUESTIONS
from techweb_user.models import TechWebUser


class Command(BaseCommandMixin):
    help = _("Seed users for development only")

    def add_arguments(self, parser):
        parser.add_argument(
            "-c", "--count", type=int, help="Rows count", required=False, default=10
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                count = int(options.get("count"))
                faker = Faker()
                for _ in range(count):
                    data = {
                        "first_name": faker.first_name(),
                        "last_name": faker.last_name(),
                        "email": faker.email(),
                        "employee_id": secrets.randbelow(1000000000),
                        "token": secrets.token_urlsafe(10),
                        "user_type": random.choice(TechWebUserTypeChoices.choices)[0],
                    }
                    # DebuggingPrint.pprint(data)
                    new_user = TechWebUser.objects.create(**data)
                    new_user.set_password("test123456")
                    new_user.save()
                    DebuggingPrint.pprint(f"User {new_user} created successfully")
        except Exception as ex:
            self.stdout_output("error", str(ex))
