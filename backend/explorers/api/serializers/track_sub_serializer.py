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
    'photo_relations',
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



# Track to Photo relation serializer:
class TrackToPhotoRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Track to Photo relation.
    """

    # Other object relation schemas:
    photo = PhotoRelationSerializer(
        help_text=TrackToPhotoModel.photo.field.help_text,
        required=TrackToPhotoModel.photo.field.null,
        allow_null=TrackToPhotoModel.photo.field.blank,
    )

    class Meta:
        model = TrackModel.photos.through
        fields = [
            'id',
            'created',
            'updated',
            'track',
            'photo',
            'is_primary',
        ]
        read_only_fields = [
            'id',
            'created',
            'updated',
        ]
