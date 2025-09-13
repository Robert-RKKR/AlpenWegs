# Rest framework serializer import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_object_representation_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_object_representation_fields,
    base_creator_fields,
    base_model_fields,
)

# AlpenWegs application import:
from notifications.models.change_log_model import ChangeLogModel

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField


# ChangeLog Model serializer details:
model = ChangeLogModel
depth = 0

# Change Log Model serializer fields:
change_log_fields = [
    'action_type',
    'timestamp',
    'after',
]
change_log_read_only_fields = [
    'action_type',
    'timestamp',
    'after',
]

# Change Log model serializer combined fields:
fields = (
    base_model_fields
    + base_object_representation_fields
    + base_creator_fields
    + change_log_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_object_representation_read_only_fields
    + base_creator_read_only_fields
    + change_log_read_only_fields
)

# ChangeLog Model representation serializer fields:
representation_fields = [
    'url',
    'object_repr',
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
        fields = [field for field in fields if field != 'after']

        # Define related model:
        model = model

        # Define model depth:
        depth = depth
