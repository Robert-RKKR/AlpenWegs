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
from assets.models.photo_model import PhotoModel

# Photo Model serializer details:
model = PhotoModel
depth = 0

# Photo Model serializer fields:
photo_fields = [
    'format',
    'path',
]

# Photo model serializer combined fields:
fields = (
    base_model_fields
    + base_identification_fields
    + base_timestamp_fields
    + base_creator_fields
    + photo_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_identification_read_only_fields
    + base_timestamp_read_only_fields
    + base_creator_read_only_fields
)


# Photo Detailed serializer:
class PhotoDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Photo model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Photo object
    are required.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-assets:photo_model-detail',
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


# Photo Detailed serializer:
class PhotoRepresentationSerializer(
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
        view_name='api-assets:photo_model-detail',
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


# Photo relation serializer:
class PhotoRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Photo model. Includes all fields of
    the Photo model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Photo model is needed, not its full details.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-assets:photo_model-detail',
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
