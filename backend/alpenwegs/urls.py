# API import:
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularAPIView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

# Test import:
from rest_framework_simplejwt.views import TokenRefreshView
from alpenwegs.ashared.api.base_response_not_found import base_page_not_found

urlpatterns = [
    
    # Admin:
    path('admin/', admin.site.urls),

    # API schema registration:
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api_docs'),
    path('api/rdocs/', SpectacularRedocView.as_view(url_name='api-schema'), name='api_rdocs'),

    # API authentication and registration:
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API endpoints:
    path('api/notifications/', include('notifications.api.urls')),
    path('api/compendiums/', include('compendiums.api.urls')),
    path('api/explorers/', include('explorers.api.urls')),
    path('api/profiles/', include('profiles.api.urls')),
    path('api/assets/', include('assets.api.urls')),
]

handler404 = base_page_not_found

# Register media files serving during development:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
