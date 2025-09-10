# AlpenWegs application import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
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
representation_fields = [
    'url',
]


# Notification Model Detailed serializer class:
class NotificationDetailedSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:notification_model-detail',
        help_text='URL to provided object.',
        read_only=False,
    )

    class Meta:

        # Define read only fields:
        read_only_fields = read_only_fields

        # Define writable fields:
        fields = fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth


# Notification Representation serializer:
class NotificationRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Notification model. Includes only the fields
    necessary for representing a Notification object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Notification object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-notification:notification_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:

        # Define read only fields:
        read_only_fields = representation_fields

        # Define writable fields:
        fields = representation_fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth


# Notification relation serializer:
class NotificationRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Notification model. Includes all fields of
    the Notification model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Notification model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-notification:notification_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:

        # Define read only fields:
        read_only_fields = read_only_fields

        # Define writable fields:
        fields = fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth
