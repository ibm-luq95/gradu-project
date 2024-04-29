# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
import traceback

from django.http import HttpRequest
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.developments.debugging_print_object import DebuggingPrint

from django.views.generic import TemplateView

from home.forms import ContactForm
from home.serializers import ContactMessagesSerializer


class ContactView(TemplateView):
    template_name = "home/contact.html"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Contact us"))

        return context


class ContactAPIView(APIView):
    def post(self, request: HttpRequest, format=None):
        # Note how we access the `data` property of the `request` param.
        # It contains the values submitted in the body of the request.
        response = {}
        try:
            data = request.data.copy()
            obj = ContactMessagesSerializer(data=data)
            if obj.is_valid(raise_exception=True):
                obj.save()
                response["msg"] = _("Message sent successfully")
            return Response(data=response, status=status.HTTP_200_OK)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
