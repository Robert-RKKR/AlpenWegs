# API import:
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularAPIView

# Django import:
from django.contrib import admin
from django.urls import path

# Test import:
from notifications.test_view import NotifyMeView

urlpatterns = [

    # API - token generator registration:
    path('api-admin/token-generate/', obtain_auth_token, name='token_generate'),

    # API - schema registration:
    path('api-schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api-docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api_docs'),
    path('api-rdocs/',
        SpectacularRedocView.as_view(url_name='api-schema'),
        name='api_rdocs'),

    # Admin site URL:
    path('admin/', admin.site.urls),

    # Test notification URL:
    path('notify-me/', NotifyMeView.as_view(), name='notify-me'),
]
