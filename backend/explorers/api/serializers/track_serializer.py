# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    SerializedPkRelatedField,
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_identification_read_only_fields,
    base_sport_category_read_only_fields,
    base_statistic_read_only_fields,
    base_timestamp_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_score_read_only_fields,
    base_identification_fields,
    base_representation_fields,
    base_sport_category_fields,
    base_statistic_fields,
    base_timestamp_fields,
    base_creator_fields,
    base_model_fields,
    base_score_fields,
)

# AlpenWegs application import:
from alpenwegs.ashared.constants.sport_category_difficulty import SportCategoryDifficultyChoices
from explorers.api.serializers.route_serializer import RouteRepresentationSerializer
from explorers.api.serializers.journey_serializer import JourneyRelationSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from alpenwegs.ashared.constants.sport_category import SportCategoryChoices
from assets.api.serializers.file_serializer import FileRelationSerializer
from explorers.models.journey_model import JourneyModel
from explorers.models.track_model import TrackModel
from explorers.models.route_model import RouteModel
from assets.models.file_model import FileModel

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework import serializers


# Track Model serializer details:
model = TrackModel
depth = 0

# Track Model serializer fields:
track_fields = [
    'verified',
    'similarity_index',
    'user_notes',
    'snow_track',
    'night_track',
    'fog_track',
    'rain_track',
    'hot_weather_track',
    'cold_weather_track',
    'windy_track',
    'group_track',
    'organized_track',
    'leader_track',
    'guided_tour_track',
    'backpacking_track',
    'fast_hike_track',
    'training_track',
    'exploration_track',
    'hazardous_track',
    'injury_occurred',
    'rescue_assistance',
    'journey',
    'route',
    'gpx_data',
]

# Track model serializer combined fields:
fields = (
    base_model_fields
    + base_identification_fields
    + base_sport_category_fields
    + base_timestamp_fields
    + base_statistic_fields
    + base_creator_fields
    + base_score_fields
    + track_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_identification_read_only_fields
    + base_sport_category_read_only_fields
    + base_statistic_read_only_fields
    + base_timestamp_read_only_fields
    + base_creator_read_only_fields
    + base_score_read_only_fields
)


# Track Detailed serializer:
class TrackDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Track model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Track object
    are required.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:track_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth

    # Other object relation schemas:
    creator = UserRelationSerializer(
        help_text=TrackModel.creator.field.help_text,
        required=TrackModel.creator.field.null,
        allow_null=TrackModel.creator.field.blank,
    )

    # Other object Many to Many relation schemas:
    journey = SerializedPkRelatedField(
        queryset=JourneyModel.objects.all(),
        serializer=JourneyRelationSerializer,
        required=False,
        allow_null=True,
        many=True,
    )
    route = SerializedPkRelatedField(
        queryset=RouteModel.objects.all(),
        serializer=RouteRepresentationSerializer,
        required=False,
        allow_null=True,
        many=True,
    )
    gpx_data = SerializedPkRelatedField(
        queryset=FileModel.objects.all(),
        serializer=FileRelationSerializer,
        required=False,
        allow_null=True,
        many=True,
    )

    # Special constance fields:
    category_specific_difficulty = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    # Special constance methods:
    def get_category_specific_difficulty(self, obj):
        """
        Convert integer value into full metadata dict.
        """

        # Return metadata dict for country:
        return SportCategoryDifficultyChoices.dict_from_int(
            obj.category_specific_difficulty
        )
    
    def get_category(self, obj):
        """
        Convert integer value into full metadata dict.
        """

        # Return metadata dict for country:
        return SportCategoryChoices.dict_from_int(obj.category)


# Track Representation serializer:
class TrackRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Track model. Includes only the fields
    necessary for representing a Track object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Track object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-explorers:track_model-detail',
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


# Track relation serializer:
class TrackRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Track model. Includes all fields of
    the Track model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Track model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:track_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    # Special constance fields:
    category_specific_difficulty = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    # Special constance methods:
    def get_category_specific_difficulty(self, obj):
        """
        Convert integer value into full metadata dict.
        """

        # Return metadata dict for country:
        return SportCategoryDifficultyChoices.dict_from_int(
            obj.category_specific_difficulty
        )
    
    def get_category(self, obj):
        """
        Convert integer value into full metadata dict.
        """

        # Return metadata dict for country:
        return SportCategoryChoices.dict_from_int(obj.category)

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth
