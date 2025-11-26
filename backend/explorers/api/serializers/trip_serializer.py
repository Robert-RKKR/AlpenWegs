# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    SerializedPkRelatedField,
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_identification_read_only_fields,
    base_sport_category_read_only_fields,
    base_descriptive_read_only_fields,
    base_statistic_read_only_fields,
    base_timestamp_read_only_fields,
    base_multi_day_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_score_read_only_fields,
    base_identification_fields,
    base_representation_fields,
    base_sport_category_fields,
    base_descriptive_fields,
    base_statistic_fields,
    base_timestamp_fields,
    base_multi_day_fields,
    base_creator_fields,
    base_model_fields,
    base_score_fields,
)

# AlpenWegs application import:
from alpenwegs.ashared.constants.accommodation_type import AccommodationTypeChoices
from explorers.api.serializers.route_serializer import RouteRelationSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from explorers.models.route_model import RouteModel
from explorers.models.trip_model import TripModel

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework import serializers


# Trip Model serializer details:
model = TripModel
depth = 0

# Trip Model serializer fields:
trip_fields = [
    'routes',
]

# Trip model serializer combined fields:
fields = (
    base_model_fields
    + base_sport_category_fields
    + base_identification_fields
    + base_descriptive_fields
    + base_timestamp_fields
    + base_multi_day_fields
    + base_statistic_fields
    + base_creator_fields
    + base_score_fields
    + trip_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_sport_category_read_only_fields
    + base_identification_read_only_fields
    + base_descriptive_read_only_fields
    + base_timestamp_read_only_fields
    + base_statistic_read_only_fields
    + base_multi_day_read_only_fields
    + base_creator_read_only_fields
    + base_score_read_only_fields
)


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

    # Other object relation schemas:
    creator = UserRelationSerializer(
        help_text=TripModel.creator.field.help_text,
        required=TripModel.creator.field.null,
        allow_null=TripModel.creator.field.blank,
    )

    # Other object Many to Many relation schemas:
    routes = SerializedPkRelatedField(
        queryset=RouteModel.objects.all(),
        serializer=RouteRelationSerializer,
        required=False,
        allow_null=True,
        many=True,
    )

    # Special constance fields:
    accommodation = serializers.SerializerMethodField()

    # Special constance methods:
    def get_accommodation(self, obj):
        # Return metadata dict for country:
        return AccommodationTypeChoices.dict_from_int(
            obj.accommodation
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
        read_only_fields = base_representation_fields

        # Define writable fields:
        fields = base_representation_fields

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

    # Special constance fields:
    accommodation = serializers.SerializerMethodField()

    # Special constance methods:
    def get_accommodation(self, obj):
        # Return metadata dict for country:
        return AccommodationTypeChoices.dict_from_int(
            obj.accommodation
        )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth
