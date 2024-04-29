# -*- coding: utf-8 -*-#
import traceback
import calendar

from django.http import HttpRequest
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from classification.models import Classification
from core.choices.survey import SurveyDepartmentsTypeChoices
from core.utils.developments.debugging_print_object import DebuggingPrint
from survey.models import Survey


class DashboardAPIView(APIView):
    def post(self, request: HttpRequest, format=None):
        # Note how we access the `data` property of the `request` param.
        # It contains the values submitted in the body of the request.
        response = {}
        try:
            survey_chart_data = {}
            quarter_chart_data = dict()
            quarter_chart_data["months"] = list(calendar.month_abbr[1:])
            classification_chart_data = []
            departments_chart_data = []
            for d_slug in SurveyDepartmentsTypeChoices.choices:
                departments_chart_data.append(
                    {
                        "slug": d_slug[0],
                        "count": Survey.objects.filter(department__in=[d_slug[0]]).count(),
                        "label": d_slug[1],
                    }
                )
            all_classifications = Classification.objects.all()
            for classification in all_classifications:
                classification_chart_data.append(
                    {
                        "slug": classification.slug,
                        "label": classification.label,
                        "surveys_count": classification.surveys.count(),
                    }
                )
            response["classification_chart_data"] = classification_chart_data
            response["departments_chart_data"] = departments_chart_data
            response["quarter_chart_data"] = quarter_chart_data
            return Response(data=response, status=status.HTTP_200_OK)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
