# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_identification_read_only_fields,
    base_timestamp_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_identification_fields,
    base_representation_fields,
    base_timestamp_fields,
    base_creator_fields,
    base_model_fields,
)

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from assets.models.file_model import FileModel


# File Model serializer details:
model = FileModel
depth = 0

# File Model serializer fields:
file_fields = [
    'format',
    'path',
]

# File model serializer combined fields:
fields = (
    base_model_fields
    + base_identification_fields
    + base_timestamp_fields
    + base_creator_fields
    + file_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_identification_read_only_fields
    + base_timestamp_read_only_fields
    + base_creator_read_only_fields
)


# File Detailed serializer:
class FileDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the File model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a File object
    are required.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-assets:file_model-detail',
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


# File Representation serializer:
class FileRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the File model. Includes only the fields
    necessary for representing a File object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a File object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-assets:file_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:

        # Define read only fields:
        read_only_fields = base_representation_fields

        # Define writable fields:
        fields = base_representation_fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth


# File relation serializer:
class FileRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the File model. Includes all fields of
    the File model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the File model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-assets:file_model-detail',
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
