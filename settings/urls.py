from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf import settings
from django.conf.urls.static import static

from temp.views import TempViewSet


urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
# ------------------------------------------------
# API-Endpoints
#
router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register(
    'temp', TempViewSet
)
urlpatterns += [
    path(
        'api/v1/',
        include(router.urls)
    ),
]
