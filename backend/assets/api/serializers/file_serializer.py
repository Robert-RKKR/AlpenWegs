# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from assets.models.file_model import FileModel


# File Model serializer details:
model = FileModel
depth = 0
fields = [
    # BaseModel values:
    'pk',
    'url',

    # BaseIdentificationModel values:
    'name',
    'slug',
    'snippet',

    # BaseCreatorModel values:
    'creator',
    'is_public',

    # BaseTimestampModel values:
    'created',
    'updated',

    # FileModel file values:
    'file',
    'format',
]
read_only_fields = [
    'pk',
    'url',
    'slug',
    'creator',
    'created',
    'updated',
]
representation_fields = [
    'pk',
    'url',
    'name',
]


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
        read_only_fields = representation_fields

        # Define writable fields:
        fields = representation_fields

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
