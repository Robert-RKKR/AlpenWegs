# AlpenWegs application import:
from explorers.models.section_model import SectionModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Section Model filter class:
class SectionFilter(
    BaseFilter,
):

    class Meta:

        model = SectionModel
        fields = {
            # BaseModel values:
            'id': ['exact'],

            # BaseCharacteristicModel values:
            'potential_risk_requirement': ['exact', 'icontains'],
            'potential_risk_description': ['exact', 'icontains'],
            'experience_requirement': ['exact', 'icontains'],
            'stamina_requirement': ['exact', 'icontains'],
            'estimated_duration': ['exact', 'lt', 'gt'],
            'difficulty': ['exact', 'icontains'],
            'best_seasons': ['exact', 'icontains'],
            'best_months': ['exact', 'icontains'],
            'family_friendly': ['exact'],
            'winter_season': ['exact'],
            'summer_season': ['exact'],

            # BaseIdentificationModel values:
            'snippet': ['exact', 'icontains'],
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],

            # BaseSportCategoryModel values:
            'category': ['exact'],
            'category_specific_difficulty': ['exact'],

            # BaseDescriptiveModel values:
            'description': ['exact', 'icontains'],

            # BaseTimestampModel values:
            'created': ['exact', 'lt', 'gt'],
            'updated': ['exact', 'lt', 'gt'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseGpxModel values:
            'highest_elevation': ['exact', 'lt', 'gt'],
            'lowest_elevation': ['exact', 'lt', 'gt'],
            'elevation_gain': ['exact', 'lt', 'gt'],
            'elevation_loss': ['exact', 'lt', 'gt'],
            'total_distance': ['exact', 'lt', 'gt'],
            'average_grade': ['exact', 'lt', 'gt'],
            'highest_grade': ['exact', 'lt', 'gt'],
            'total_points': ['exact', 'lt', 'gt'],
        }
