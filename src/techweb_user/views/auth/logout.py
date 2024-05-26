# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import RedirectView


class TWLogoutView(RedirectView):
    """
    Provides users the ability to logout
    """

    url = reverse_lazy("home:home")

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, _("You are now logged out successfully."))
        return super(TWLogoutView, self).get(request, *args, **kwargs)
