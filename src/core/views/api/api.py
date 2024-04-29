# -*- coding: utf-8 -*-#
from django.urls import reverse_lazy
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils.developments.debugging_print_object import DebuggingPrint


class FetchUrlApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            url_name = data.get("urlName")
            pk = data.get("pk", None)
            if pk is not None:
                url_path = reverse_lazy(url_name, kwargs={"pk": pk})
            else:
                url_path = reverse_lazy(url_name)
            return Response(
                {"urlPath": url_path},
                status=status.HTTP_200_OK,
            )
        except APIException as ex:
            # logger.error("API Exception")
            return Response(ex.default_detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            DebuggingPrint.print_exception()
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while fetch url name!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
