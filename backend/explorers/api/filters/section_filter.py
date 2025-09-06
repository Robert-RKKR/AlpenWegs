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

            # BaseIdentificationModel values:
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'snippet': ['exact', 'icontains'],

            # BaseDescriptiveModel values:
            'description': ['exact', 'icontains'],

            # BaseCharacteristicModel values:
            'difficulty': ['exact', 'icontains'],
            'stamina_requirement': ['exact', 'icontains'],
            'experience_requirement': ['exact', 'icontains'],
            'potential_risk_requirement': ['exact', 'icontains'],
            'potential_risk_description': ['exact', 'icontains'],
            'family_friendly': ['exact'],
            'best_seasons': ['exact', 'icontains'],
            'best_months': ['exact', 'icontains'],
            'winter_season': ['exact'],
            'summer_season': ['exact'],

            # BaseSportCategoryModel values:
            'category': ['exact'],
            'category_specific_difficulty': ['exact'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseTimestampModel values:
            'created': ['exact', 'lt', 'gt'],
            'updated': ['exact', 'lt', 'gt'],
        }
