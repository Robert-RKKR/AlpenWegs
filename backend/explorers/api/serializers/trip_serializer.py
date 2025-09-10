# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from explorers.models.trip_model import TripModel


# Trip Model serializer details:
model = TripModel
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

    # BaseSportCategoryModel values:
    'category',
    'category_specific_difficulty',

    # Trip-specific values:
    'days',

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


# Trip Detailed serializer:
class TripDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Trip model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Trip object
    are required.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:trip_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth


# Trip Representation serializer:
class TripRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Trip model. Includes only the fields
    necessary for representing a Trip object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Trip object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-explorers:trip_model-detail',
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


# Trip relation serializer:
class TripRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Trip model. Includes all fields of
    the Trip model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Trip model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:trip_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth
