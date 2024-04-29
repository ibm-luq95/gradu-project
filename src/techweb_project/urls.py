"""
URL configuration for techweb_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

static_and_media_path_urls = static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path("", include("home.urls"), name="home"),
    path("survey/", include("survey.urls"), name="survey"),
    path("employee/", include("employee.urls"), name="employee"),
    path("dashboard/", include("dashboard.urls"), name="dashboard"),
    path("core/", include("core.urls"), name="core"),
]
urlpatterns += static_and_media_path_urls
if settings.DEBUG:

    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns.append(path("admin/", admin.site.urls))
    urlpatterns.append(path("admin/doc/", include("django.contrib.admindocs.urls")))
else:
    urlpatterns.append(path("secret/", admin.site.urls))
