# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    SerializedPkRelatedField,
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_identification_read_only_fields,
    base_sport_category_read_only_fields,
    base_timestamp_read_only_fields,
    base_statistic_read_only_fields,
    base_gpx_track_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_score_read_only_fields,
    base_identification_fields,
    base_representation_fields,
    base_sport_category_fields,
    base_gpx_read_only_fields,
    base_timestamp_fields,
    base_statistic_fields,
    base_gpx_track_fields,
    base_creator_fields,
    base_model_fields,
    base_score_fields,
    base_gpx_fields,
)

# AlpenWegs application import:
from alpenwegs.ashared.constants.sport_category_difficulty import SportCategoryDifficultyChoices
from explorers.api.serializers.route_serializer import RouteRepresentationSerializer
from explorers.api.serializers.journey_serializer import JourneyRelationSerializer
from compendiums.api.serializers.poi_serializer import PoiRelationSerializer
from assets.api.serializers.photo_serializer import PhotoRelationSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from alpenwegs.ashared.constants.sport_category import SportCategoryChoices
from assets.api.serializers.file_serializer import FileRelationSerializer
from explorers.models.track_model import TrackToPhotoModel
from explorers.models.track_model import TrackModel
from compendiums.models.poi_model import PoiModel
from assets.models.photo_model import PhotoModel

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
    'start_poi',
    'end_poi',
    'photos',
    'pois',
]

# Track model serializer combined fields:
fields = (
    base_model_fields
    + base_identification_fields
    + base_sport_category_fields
    + base_timestamp_fields
    + base_statistic_fields
    + base_gpx_track_fields
    + base_creator_fields
    + base_score_fields
    + base_gpx_fields
    + track_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_identification_read_only_fields
    + base_sport_category_read_only_fields
    + base_statistic_read_only_fields
    + base_timestamp_read_only_fields
    + base_gpx_track_read_only_fields
    + base_creator_read_only_fields
    + base_score_read_only_fields
    + base_gpx_read_only_fields
)

# Track Relation serializer fields:
fields_relation = fields.copy()
fields_relation.remove('elevation_graph')
fields_relation.remove('gpx_data')
fields_relation.remove('geojson')


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

    # Other object Many to Many relation schemas:
    photos = SerializedPkRelatedField(
        queryset=PhotoModel.objects.all(),
        serializer=PhotoRelationSerializer,
        required=False,
        allow_null=True,
        many=True,
    )
    pois = SerializedPkRelatedField(
        queryset=PoiModel.objects.all(),
        serializer=PoiRelationSerializer,
        required=False,
        allow_null=True,
        many=True,
    )

    # Other object relation schemas:
    start_poi = PoiRelationSerializer(
        help_text=TrackModel.start_poi.field.help_text,
        required=TrackModel.start_poi.field.null,
        allow_null=TrackModel.start_poi.field.blank,
    )
    end_poi = PoiRelationSerializer(
        help_text=TrackModel.end_poi.field.help_text,
        required=TrackModel.end_poi.field.null,
        allow_null=TrackModel.end_poi.field.blank,
    )
    creator = UserRelationSerializer(
        help_text=TrackModel.creator.field.help_text,
        required=TrackModel.creator.field.null,
        allow_null=TrackModel.creator.field.blank,
    )
    journey = JourneyRelationSerializer(
        help_text=TrackModel.journey.field.help_text,
        required=False,
        allow_null=True,
    )
    route = RouteRepresentationSerializer(
        help_text=TrackModel.route.field.help_text,
        required=False,
        allow_null=True,
    )
    gpx_data = FileRelationSerializer(
        help_text=TrackModel.gpx_data.field.help_text,
        required=False,
        allow_null=True,
    )

    # Special constance fields:
    category_specific_difficulty = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    # Special constance methods:
    def get_category_specific_difficulty(self, obj):
        # Return metadata dict for country:
        return SportCategoryDifficultyChoices.dict_from_int(
            obj.category_specific_difficulty
        )
    
    def get_category(self, obj):
        # Return metadata dict for country:
        return SportCategoryChoices.dict_from_int(
            obj.category
        )


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
        read_only_fields = base_representation_fields + ['name']

        # Define writable fields:
        fields = base_representation_fields + ['name']

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
        # Return metadata dict for country:
        return SportCategoryDifficultyChoices.dict_from_int(
            obj.category_specific_difficulty
        )
    
    def get_category(self, obj):
        # Return metadata dict for country:
        return SportCategoryChoices.dict_from_int(obj.category)

    # Virtual not existing in DB fields:
    primary_photo = serializers.SerializerMethodField()

    # Virtual not existing in DB fields methods:
    def get_primary_photo(self, obj):
        
        # Get primary photo relation:
        rel = (
            obj.photo_track_associations
               .filter(is_primary=True)
               .select_related('photo')
               .first()
        )
        # Return None if no primary photo:
        if not rel:
            return None
        # Return primary photo data:
        return {
            'id': rel.photo.id,
            'url': rel.photo.file.url,
        }

    class Meta:
        read_only_fields = read_only_fields
        fields = fields_relation + ['primary_photo']
        model = model
        depth = depth

# Track to Photo relation serializer:
class TrackToPhotoRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Track to Photo relation.
    """

    # Other object relation schemas:
    track = TrackRepresentationSerializer(
        help_text=TrackToPhotoModel.track.field.help_text,
        required=TrackToPhotoModel.track.field.null,
        allow_null=TrackToPhotoModel.track.field.blank,
    )
    photo = PhotoRelationSerializer(
        help_text=TrackToPhotoModel.photo.field.help_text,
        required=TrackToPhotoModel.photo.field.null,
        allow_null=TrackToPhotoModel.photo.field.blank,
    )

    class Meta:
        model = TrackModel.photos.through
        fields = [
            'id',
            'track',
            'photo',
            'is_primary',
        ]
        read_only_fields = [
            'id',
        ]
