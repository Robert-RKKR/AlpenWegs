# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    SerializedPkRelatedField,
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_identification_read_only_fields,
    base_descriptive_read_only_fields,
    base_timestamp_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_identification_fields,
    base_representation_fields,
    base_descriptive_fields,
    base_timestamp_fields,
    base_creator_fields,
    base_model_fields,
)

# AlpenWegs application import:
from compendiums.api.serializers.region_serializer import RegionRelationSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from explorers.models.section_model import SectionModel
from compendiums.models.poi_model import PoiModel

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField


# PoI Model serializer details:
model = PoiModel
depth = 0

# PoI Model serializer fields:
poi_fields = [
    'transport_description',
    'location',
    'elevation',
    'category',
    'region',
]

# PoI model serializer combined fields:
fields = (
    base_model_fields
    + base_identification_fields
    + base_descriptive_fields
    + base_timestamp_fields
    + base_creator_fields
    + poi_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_identification_read_only_fields
    + base_descriptive_read_only_fields
    + base_timestamp_read_only_fields
    + base_creator_read_only_fields
)
where_used_fields = (
    base_model_fields
    + ['sections']
)
where_used_read_only_fields = (
    base_model_read_only_fields
    + ['sections']
)


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
        read_only_fields = base_representation_fields

        # Define writable fields:
        fields = base_representation_fields

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


# Poi Where Used serializer:
class PoiWhereUsedSerializer(
    BaseSerializer,
):
    """
    Where Used serializer for the Poi model. Includes fields
    that identify where the PoI object is used. Collecting
    data based on relations with other Models.

    Used for retrieve API actions.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-compendiums:poi_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    # Other object relation schemas:
    sections = SerializedPkRelatedField(
        queryset=SectionModel.objects.all(),
        serializer='explorers.api.serializers.section_serializer.SectionRelationSerializer',
        required=False,
        allow_null=True,
        many=True,
    )

    class Meta:

        # Define read only fields:
        read_only_fields = where_used_read_only_fields

        # Define writable fields:
        fields = where_used_fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth
