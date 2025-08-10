# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# AlpenWegs application import:
from profiles.models.member_model import MemberModel

# Rest framework serializer import:
from rest_framework.serializers import HyperlinkedIdentityField


# Member Model serializer details:
model = MemberModel
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
    # Member Model:
    'last_login',
    'is_staff',
    'is_superuser',
    'name',
    'email',
    'groups',
    'user_permissions',
]


# Member Model serializer class:
class MemberSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-management:member_model-detail',
        help_text='URL to provided object.',
        read_only=False
    )

    class Meta:

        model = model
        fields = fields
        extra_kwargs = {'password': {'write_only': True}}


# Member Model nested serializer class:
class MemberNestedSerializer(WritableNestedSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-management:member_model-detail',
        help_text='URL to provided object.',
        read_only=False
    )

    class Meta:

        model = model
        fields = fields
        extra_kwargs = {'password': {'write_only': True}}
