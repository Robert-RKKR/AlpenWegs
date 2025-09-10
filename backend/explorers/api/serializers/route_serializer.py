# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from explorers.models.route_model import RouteModel


# Route Model serializer details:
model = RouteModel
depth = 0
fields = [
    # BaseModel values:
    'pk',
    'url',

    # BaseIdentificationModel values:
    'name',
    'slug',
    'snippet',

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

    # BaseStatisticModel values:
    'comment_count',
    'visit_count',
    'download_count',

    # BaseScoreModel values:
    'score',

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


# Route Detailed serializer:
class RouteDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Route model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Route object
    are required.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:route_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth


# Route Representation serializer:
class RouteRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Route model. Includes only the fields
    necessary for representing a Route object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Route object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-explorers:route_model-detail',
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


# Route relation serializer:
class RouteRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Route model. Includes all fields of
    the Route model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Route model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:route_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth
