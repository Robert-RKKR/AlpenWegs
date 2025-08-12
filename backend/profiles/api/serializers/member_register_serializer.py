from dj_rest_auth.registration.serializers import RegisterSerializer

class MemberRegisterSerializer(RegisterSerializer):
    _has_phone_field = False
