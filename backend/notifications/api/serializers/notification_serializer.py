# AlpenWegs application import:
from notifications.models.notification_model import NotificationModel

# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# Rest framework serializer import:
from rest_framework.serializers import HyperlinkedIdentityField


# Notification Model serializer details:
model = NotificationModel
depth = 0
fields = [
    # Base Model values:
    'pk',
    'url',
    # Base notification data:
    'timestamp',
    'severity',
    'task_id',
    'message',
    'object_url',
]
read_only_fields = [
    # Base Model values:
    'pk',
    'url',
    # Base notification data:
    'timestamp',
    'severity',
    'task_id',
    'message',
    'object_url',
]


# Notification Model serializer class:
class NotificationSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:notification_model-detail',
        help_text='URL to provided object.',
        read_only=False,
    )

    class Meta:

        model = model
        depth = depth
        fields = fields
        read_only_fields = read_only_fields
