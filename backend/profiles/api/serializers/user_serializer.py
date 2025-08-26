# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# Rest framework serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from profiles.models.user_model import UserModel


# User Model serializer details:
model = UserModel
fields = [
    # Default:
    'pk',
    'url',
    # Timestamp model values:
    'created',
    'updated',
    # Required User fields:
    'is_active',
    'is_staff',
    'last_login',
    'is_superuser',
    # Base User identification information:
    'email',
    'username',
    'first_name',
    'middle_name',
    'last_name',
    # Password information:
    'password_to_change',
    # Contact information:
    'phone_number',
    # Personal information:
    'gender',
    'weight',
    'height',
    'bmi',
    'birthday',
    # Location information:
    'location',
    'location_name',
]


# User Model serializer class:
class UserSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-profiles:user_model-detail',
        help_text='URL to provided object.',
        read_only=False
    )

    class Meta:

        model = model
        fields = fields


# User Model nested serializer class:
class UserNestedSerializer(WritableNestedSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-profiles:user_model-detail',
        help_text='URL to provided object.',
        read_only=False
    )

    class Meta:

        model = model
        fields = fields
