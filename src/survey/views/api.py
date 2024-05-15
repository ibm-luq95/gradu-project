# -*- coding: utf-8 -*-#
import traceback

from django.http import HttpRequest
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.developments.debugging_print_object import DebuggingPrint
from techwell_model.backend_model.model import TechWellModel


class SurveyAPIView(APIView):
    def post(self, request: HttpRequest, format=None):
        # Note how we access the `data` property of the `request` param.
        # It contains the values submitted in the body of the request.
        response = {}
        try:
            full_steps_form: dict = request.data.copy()
            backend_model = TechWellModel(
                user=self.request.user,
                survey_questions=full_steps_form,
                excluded_steps=[1],
            )
            # response["result"] = backend_model.classify_responses()
            response["results"] = backend_model.run_classifier()
            return Response(data=response, status=status.HTTP_200_OK)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
