# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# AlpenWegs application import:
from profiles.models.user_model import UserModel

# Rest framework serializer import:
from rest_framework.serializers import HyperlinkedIdentityField


# User Model serializer details:
model = UserModel
fields = [
    # Default:
    'pk',
    'url',
    # Status Model:
    'is_deleted',
    'is_root',
    'is_active',
    'created',
    'updated',
    # User Model:
    'last_login',
    'is_staff',
    'is_superuser',
    'name',
    'email',
    'groups',
    'user_permissions',
]


# User Model serializer class:
class UserSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-management:user_model-detail',
        help_text='URL to provided object.',
        read_only=False
    )

    class Meta:

        model = model
        fields = fields
        extra_kwargs = {'password': {'write_only': True}}


# User Model nested serializer class:
class UserNestedSerializer(WritableNestedSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-management:user_model-detail',
        help_text='URL to provided object.',
        read_only=False
    )

    class Meta:

        model = model
        fields = fields
        extra_kwargs = {'password': {'write_only': True}}
