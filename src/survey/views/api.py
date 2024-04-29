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
            step_1_form_data: list[dict[str, str]] = full_steps_form.get("step1")
            step_2_form_data: list[dict[str, str, str]] = full_steps_form.get("step2")
            step_3_form_data: list[dict[str, str, str]] = full_steps_form.get("step3")
            step_4_form_data: list[dict[str, str, str]] = full_steps_form.get("step4")
            step_5_form_data: list[dict[str, str, str]] = full_steps_form.get("step5")
            # DebuggingPrint.pprint(request.data)
            backend_model = TechWellModel(self.request.user, request.data.copy(), [1])
            response["result"] = backend_model.classify_responses()
            DebuggingPrint.log(response["result"])
            DebuggingPrint.rule()
            return Response(data=response, status=status.HTTP_200_OK)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
