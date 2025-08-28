# Rest framework serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# AlpenWegs application import:
from notifications.models.change_log_model import ChangeLogModel


# ChangeLog Model serializer details:
model = ChangeLogModel
depth = 0
fields = [
    # Base Model values:
    'pk',
    'url',
    # Object Representation Model values:
    'app_name',
    'model_name',
    'object_id',
    'object_repr',
    # Model data time information:
    'timestamp',
    # User information:
    'user',
    # Change details:
    'action_type',
    'after',
]
read_only_fields = [
    # Base Model values:
    'pk',
    'url',
    # Object Representation Model values:
    'app_name',
    'model_name',
    'object_id',
    'object_repr',
    # Model data time information:
    'timestamp',
    # User information:
    'user',
    # Change details:
    'action_type',
    'after',
]


# ChangeLog Model serializer class:
class ChangeLogSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:change_log_model-detail',
        help_text='URL to provided object.',
        read_only=False,
    )

    class Meta:

        model = model
        depth = depth
        fields = fields
        read_only_fields = read_only_fields

# ChangeLog Model serializer class without After value:
class ChangeLogWithoutAfterSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:change_log_model-detail',
        help_text='URL to provided object.',
        read_only=False,
    )

    class Meta:

        model = model
        depth = depth
        fields = [field for field in fields if field != 'after']
        read_only_fields = read_only_fields
