# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.serializers.base_serializers import BaseSerializer

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from explorers.models.section_model import SectionModel


# Section Model serializer details:
model = SectionModel
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

    # BaseCharacteristicModel values:
    'difficulty',
    'stamina_requirement',
    'experience_requirement',
    'potential_risk_requirement',
    'potential_risk_description',
    'family_friendly',
    'best_seasons',
    'best_months',
    'winter_season',
    'summer_season',

    # BaseSportCategoryModel values:
    'category',
    'category_specific_difficulty',

    # BaseCreatorModel values:
    'creator',
    'is_public',

    # BaseTimestampModel values:
    'created',
    'updated',
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


# Section Detailed serializer:
class SectionDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Section model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Section object
    are required.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:section_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth


# Section Representation serializer:
class SectionRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Section model. Includes only the fields
    necessary for representing a Section object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Section object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-explorers:section_model-detail',
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


# Section relation serializer:
class SectionRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Section model. Includes all fields of
    the Section model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Section model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:section_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth
