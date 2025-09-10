# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from compendiums.models.region_model import RegionModel


# Region Model serializer details:
model = RegionModel
depth = 0
fields = [
    # BaseModel values:
    'pk',
    'url',

    # BaseIdentificationModel values:
    'name',
    'slug',
    'snippet',

    # BaseDescriptiveModel values:
    'description',

    # BaseCreatorModel values:
    'creator',
    'is_public',

    # BaseTimestampModel values:
    'created',
    'updated',

    # RegionModel values:
    'country',
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
    'url',
    'name',
]


# Region Detailed serializer:
class RegionDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Region model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Region object
    are required.
    """

    url = HyperlinkedIdentityField(
        view_name='api-compendiums:region_model-detail',
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


# Region Representation serializer:
class RegionRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Region model. Includes only the fields
    necessary for representing a Region object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Region object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-compendiums:region_model-detail',
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


# Region relation serializer:
class RegionRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Region model. Includes all fields of
    the Region model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Region model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-compendiums:region_model-detail',
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
