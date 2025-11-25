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
            'snippet': ['exact', 'icontains'],
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],

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
            'overall_average_speed': ['exact', 'lt', 'gt'],
            'descent_average_speed': ['exact', 'lt', 'gt'],
            'maximum_descent_speed': ['exact', 'lt', 'gt'],
            'ascent_average_speed': ['exact', 'lt', 'gt'],
            'maximum_ascent_speed': ['exact', 'lt', 'gt'],
            'moving_average_speed': ['exact', 'lt', 'gt'],
            'temperature_average': ['exact', 'lt', 'gt'],
            'average_heart_rate': ['exact', 'lt', 'gt'],
            'maximum_heart_rate': ['exact', 'lt', 'gt'],
            'minimum_heart_rate': ['exact', 'lt', 'gt'],
            'calories_burned': ['exact', 'lt', 'gt'],
            'maximum_speed': ['exact', 'lt', 'gt'],
            'minimum_speed': ['exact', 'lt', 'gt'],
            'average_speed': ['exact', 'lt', 'gt'],
            'moving_ratio': ['exact', 'lt', 'gt'],
            'pace_average': ['exact', 'lt', 'gt'],
            'steps_count': ['exact', 'lt', 'gt'],
            'moving_time': ['exact', 'lt', 'gt'],
            'total_time': ['exact', 'lt', 'gt'],
            'start_time': ['exact', 'lt', 'gt'],
            'stop_time': ['exact', 'lt', 'gt'],
            'pace_best': ['exact', 'lt', 'gt'],
            'end_time': ['exact', 'lt', 'gt'],
            'weather_conditions': ['exact'],
            'equipment_used': ['exact'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseScoreModel values:
            'score': ['exact', 'lt', 'gt'],

            # BaseGpxModel values:
            'highest_elevation': ['exact', 'lt', 'gt'],
            'lowest_elevation': ['exact', 'lt', 'gt'],
            'elevation_gain': ['exact', 'lt', 'gt'],
            'elevation_loss': ['exact', 'lt', 'gt'],
            'total_distance': ['exact', 'lt', 'gt'],
            'average_grade': ['exact', 'lt', 'gt'],
            'highest_grade': ['exact', 'lt', 'gt'],
            'total_points': ['exact', 'lt', 'gt'],
            'duration': ['exact', 'lt', 'gt'],
        }
