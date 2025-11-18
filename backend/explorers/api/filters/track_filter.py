# AlpenWegs application import:
from explorers.models.track_model import TrackModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Track Model filter class:
class TrackFilter(
    BaseFilter,
):

    class Meta:

        model = TrackModel
        fields = {
            # BaseModel values:
            'id': ['exact'],

            # BaseIdentificationModel values:
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'snippet': ['exact', 'icontains'],

            # BaseSportCategoryModel values:
            'category': ['exact'],
            'category_specific_difficulty': ['exact'],

            # BaseAccomplishedModel values:
            'accomplished_count': ['exact', 'lt', 'gt'],

            # BaseDescriptiveModel values:
            'description': ['exact', 'icontains'],

            # BaseTimestampModel values:
            'created': ['exact', 'lt', 'gt'],
            'updated': ['exact', 'lt', 'gt'],

            # BaseGpxTrackModel values:
            'start_time': ['exact', 'lt', 'gt'],
            'end_time': ['exact', 'lt', 'gt'],
            'moving_time': ['exact', 'lt', 'gt'],
            'total_time': ['exact', 'lt', 'gt'],
            'average_speed': ['exact', 'lt', 'gt'],
            'maximum_speed': ['exact', 'lt', 'gt'],
            'minimum_speed': ['exact', 'lt', 'gt'],
            'average_heart_rate': ['exact', 'lt', 'gt'],
            'maximum_heart_rate': ['exact', 'lt', 'gt'],
            'minimum_heart_rate': ['exact', 'lt', 'gt'],
            'calories_burned': ['exact', 'lt', 'gt'],
            'steps_count': ['exact', 'lt', 'gt'],
            'weather_conditions': ['exact'],
            'temperature_average': ['exact', 'lt', 'gt'],
            'equipment_used': ['exact'],
            'moving_ratio': ['exact', 'lt', 'gt'],
            'pace_average': ['exact', 'lt', 'gt'],
            'pace_best': ['exact', 'lt', 'gt'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseScoreModel values:
            'score': ['exact', 'lt', 'gt'],

            # BaseGpxModel values:
            'duration': ['exact', 'lt', 'gt'],
            'distance': ['exact', 'lt', 'gt'],
            'elevation_gain': ['exact', 'lt', 'gt'],
            'elevation_loss': ['exact', 'lt', 'gt'],
            'highest_elevation': ['exact', 'lt', 'gt'],
            'lowest_elevation': ['exact', 'lt', 'gt'],
            'average_grade': ['exact', 'lt', 'gt'],
            'highest_grade': ['exact', 'lt', 'gt'],
        }
