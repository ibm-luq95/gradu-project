# -*- coding: utf-8 -*-#
import mimetypes
from ._base import *

mimetypes.add_type("application/javascript", ".js", True)

DEBUG = config("DEBUG", cast=bool)

INSTALLED_APPS = INSTALLED_APPS + [
    "django.contrib.admindocs",
    "debug_toolbar",
    "debugtools",
    "debug_permissions",
    "django_model_info.apps.DjangoModelInfoConfig",
]

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "debugtools.middleware.XViewMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "django_pdb.middleware.PdbMiddleware",
]
# Database configurations
# DATABASES = {
#     "default": {
#         "ENGINE": config("DB_ENGINE", cast=str),
#         "NAME": config("DB_NAME", cast=str),
#         "USER": config("DB_USER", cast=str),
#         "PASSWORD": config("DB_PASSWORD", cast=str),
#         "HOST": config("DB_HOST", cast=str),
#         "PORT": config("DB_PORT", cast=str),
#         "CONN_MAX_AGE": None,
#         "OPTIONS": {
#             "client_encoding": config("DB_CLIENT_ENCODING", cast=str),
#             "server_side_binding": True,
#         },
#     }
# }


INTERNAL_IPS = config("INTERNAL_IPS", cast=Csv())

DISABLE_PANELS = {}

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debugtools.panels.ViewPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

SHOW_COLLAPSED = True
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}

GRAPH_MODELS = {"all_applications": True, "group_models": True}
# GRAPH_MODELS = {'app_labels': ["client"]}

# django-request-viewer configs
REQUEST_VIEWER = {"LIVE_MONITORING": False, "WHITELISTED_PATH": []}

X_FRAME_OPTIONS = "SAMEORIGIN"
DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}
