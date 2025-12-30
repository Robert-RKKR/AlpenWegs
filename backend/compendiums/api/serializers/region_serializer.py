# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_representation_identification_fields,
    base_identification_read_only_fields,
    base_descriptive_read_only_fields,
    base_timestamp_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_identification_fields,
    base_descriptive_fields,
    base_timestamp_fields,
    base_creator_fields,
    base_model_fields,
)
# AlpenWegs application import:
from profiles.api.serializers.user_serializer import UserRelationSerializer
from alpenwegs.ashared.constants.region_type import RegionTypeChoices
from alpenwegs.ashared.constants.country import CountryChoices
from compendiums.models.region_model import RegionModel

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework import serializers


# Region Model serializer details:
model = RegionModel
depth = 0

# Region Model serializer fields:
region_fields = [
    'country',
    'type',
]

# Region model serializer combined fields:
fields = (
    base_model_fields
    + base_identification_fields
    + base_descriptive_fields
    + base_timestamp_fields
    + base_creator_fields
    + region_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_identification_read_only_fields
    + base_descriptive_read_only_fields
    + base_timestamp_read_only_fields
    + base_creator_read_only_fields
)


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

    # Other object relation schemas:
    creator = UserRelationSerializer(
        help_text=RegionModel.creator.field.help_text,
        required=RegionModel.creator.field.null,
        allow_null=RegionModel.creator.field.blank,
    )

    # Special constance fields:
    country = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    # Special constance methods:
    def get_country(self, obj):
        """
        Convert integer value into full metadata dict.
        """

        # Return metadata dict for country:
        return CountryChoices.dict_from_int(obj.country)
    
    def get_type(self, obj):
        """
        Convert integer value into full metadata dict.
        """

        # Return metadata dict for country:
        return RegionTypeChoices.dict_from_int(obj.type)

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
        read_only_fields = base_representation_identification_fields

        # Define writable fields:
        fields = base_representation_identification_fields

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

    # Special constance fields:
    country = serializers.SerializerMethodField()

    # Special constance methods:
    def get_country(self, obj):
        """
        Convert integer value into full metadata dict.
        """

        # Return metadata dict for country:
        return CountryChoices.dict_from_int(obj.country)

    class Meta:

        # Define read only fields:
        read_only_fields = read_only_fields

        # Define writable fields:
        fields = fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth
