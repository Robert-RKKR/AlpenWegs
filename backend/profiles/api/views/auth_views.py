# Rest framework import:
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.utils import extend_schema_view
from drf_spectacular.utils import extend_schema


class AuthTokenRefreshView(TokenRefreshView):
    
    pass
