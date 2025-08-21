# Rest framework import:
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


# User registration serializer class:
class UserRegisterSerializer(RegisterSerializer):

    _has_phone_field = False
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        """
        Called after user is created. We can add extra fields here.
        """

        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name', 'last_name'])
        return user
    
from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class WorkingJWTLoginSerializer(BaseLoginSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        self.user = self.user  # needed for refresh generation

        refresh = RefreshToken.for_user(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
    
from dj_rest_auth.serializers import LoginSerializer

class DebugJWTSerializer(LoginSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print("DEBUG: Custom LoginSerializer used.")
        return data
