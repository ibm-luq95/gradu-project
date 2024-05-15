# -*- coding: utf-8 -*-#
from django.shortcuts import render


def custom_500(request):
    return render(request, "errors/500.html", status=500)
