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
                departments_chart_data.append({
                    "slug": d_slug[0],
                    "count": Survey.objects.filter(department__in=[d_slug[0]]).count(),
                    "label": d_slug[1],
                })
            all_classifications = Classification.objects.all()
            for classification in all_classifications:
                classification_chart_data.append({
                    "slug": classification.slug,
                    "label": classification.label,
                    "surveys_count": classification.surveys.count(),
                })
            response["classification_chart_data"] = classification_chart_data
            response["departments_chart_data"] = departments_chart_data
            response["quarter_chart_data"] = quarter_chart_data
            all_departments = []
            for dep in SurveyDepartmentsTypeChoices.choices:
                all_departments.append(dep[1])
            response["all_departments"] = all_departments
            months_idx = list(range(1, 13, 1))
            DebuggingPrint.pprint(months_idx)
            all_surveys = Survey.objects.all()
            # for a in all_surveys:
            # DebuggingPrint.pprint(a.created_at)
            # DebuggingPrint.pprint(a.created_at.month)
            department_data = []
            for midx in months_idx:
                DebuggingPrint.log(midx)
                alls = Survey.objects.filter(created_at__month=midx)
                DebuggingPrint.print(alls)
                DebuggingPrint.print(alls.count())
                for department in SurveyDepartmentsTypeChoices.choices:
                    department_code = department[0]
                    DebuggingPrint.pprint(department_code)
                    department_qs = alls.filter(department=department_code)
                    DebuggingPrint.pprint(department_qs)
                department_data.append(
                    {"month_idx": midx, "month_abbr": calendar.month_abbr[midx]}
                )
                DebuggingPrint.rule()
            # for department in SurveyDepartmentsTypeChoices.choices:
            #     DebuggingPrint.pprint(department)
            #     for midx in months_idx:
            #         # DebuggingPrint.pprint(midx)
            #         q = Survey.objects.filter(
            #             department=department[0]
            #         )
            #         DebuggingPrint.pprint(q.first().created_at.month)
            #     # DebuggingPrint.pprint(q)
            #     DebuggingPrint.rule()
            return Response(data=response, status=status.HTTP_200_OK)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
