# Rest framework serializer import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
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
    'creator',
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
    'creator',
    # Change details:
    'action_type',
    'after',
]
representation_fields = [
    'url',
]


# ChangeLog Model Detailed serializer class:
class ChangeLogDetailedSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:change_log_model-detail',
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


# ChangeLog Representation serializer:
class ChangeLogRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the ChangeLog model. Includes only the fields
    necessary for representing a ChangeLog object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a ChangeLog object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-notification:change_log_model-detail',
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


# ChangeLog relation serializer:
class ChangeLogRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the ChangeLog model. Includes all fields of
    the ChangeLog model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the ChangeLog model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-notification:change_log_model-detail',
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


# ChangeLog Model serializer class without After value:
class ChangeLogWithoutAfterSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-notification:change_log_model-detail',
        help_text='URL to provided object.',
        read_only=False,
    )

    class Meta:

        # Define read only fields:
        read_only_fields = read_only_fields

        # Define writable fields:
        fields = [field for field in fields if field != 'after']

        # Define related model:
        model = model

        # Define model depth:
        depth = depth
