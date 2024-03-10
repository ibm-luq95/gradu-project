# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = "home/contact.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Contact us"))

        return context
