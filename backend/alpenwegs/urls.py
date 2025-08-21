# API import:
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularAPIView

# Django import:
from django.contrib import admin
from django.urls import include
from django.urls import path

# Test import:
from notifications.test_view import NotifyMeView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # API - schema registration:
    path('api-schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api-docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api_docs'),
    path('api-rdocs/', SpectacularRedocView.as_view(url_name='api-schema'), name='api_rdocs'),

    # dj-rest-auth core:
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # SimpleJWT refresh:
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Admin:
    path('admin/', admin.site.urls),

    # Test notification:
    path('notify-me/', NotifyMeView.as_view(), name='notify-me'),
]

