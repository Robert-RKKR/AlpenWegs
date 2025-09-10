# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from compendiums.api.serializers.region_serializer import RegionRelationSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from compendiums.models.poi_model import PoiModel


# PoI Model serializer details:
model = PoiModel
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

    # PoiModel values:
    'region',
    'transport_description',
    'category',
    'latitude',
    'longitude',
    'elevation',
]
read_only_fields = [
    'pk',
    'url',
    'slug',
    'created',
    'updated',
]
representation_fields = [
    'url',
    'name',
]


# PoI Detailed serializer:
class PoiDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the PoI model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a PoI object
    are required.
    """

    url = HyperlinkedIdentityField(
        view_name='api-compendiums:poi_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    # Other object relation schemas:
    creator = UserRelationSerializer(
        help_text=PoiModel.creator.field.help_text,
        required=PoiModel.creator.field.null,
        allow_null=PoiModel.creator.field.blank,
    )
    region = RegionRelationSerializer(
        help_text=PoiModel.region.field.help_text,
        required=PoiModel.region.field.null,
        allow_null=PoiModel.region.field.blank,
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


# Poi Representation serializer:
class PoiRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Poi model. Includes only the fields
    necessary for representing a Poi object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Poi object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-compendiums:poi_model-detail',
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


# PoI relation serializer:
class PoiRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the PoI model. Includes all fields of
    the PoI model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the PoI model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-compendiums:poi_model-detail',
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
