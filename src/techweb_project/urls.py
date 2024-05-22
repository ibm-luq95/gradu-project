from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import handler500

handler500 = "core.views.errors.custom_500"

static_and_media_path_urls = static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path("", include("home.urls"), name="home"),
    path("survey/", include("survey.urls"), name="survey"),
    path("dashboard/", include("dashboard.urls"), name="dashboard"),
    path("core/", include("core.urls"), name="core"),
    path("auth/", include("techweb_user.urls"), name="auth"),
]
urlpatterns += static_and_media_path_urls
if settings.DEBUG:

    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns.append(path("admin/", admin.site.urls))
    urlpatterns.append(path("admin/doc/", include("django.contrib.admindocs.urls")))
else:
    urlpatterns.append(path("secret/", admin.site.urls))
