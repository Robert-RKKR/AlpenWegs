# AlpenWegs application import:
from explorers.models.route_model import RouteModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Route Model filter class:
class RouteFilter(
    BaseFilter,
):

    class Meta:

        model = RouteModel
        fields = {
            # BaseModel values:
            'id': ['exact'],

            # BaseIdentificationModel values:
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'snippet': ['exact', 'icontains'],

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

            # BaseStatisticModel values:
            'comment_count': ['exact', 'lt', 'gt'],
            'visit_count': ['exact', 'lt', 'gt'],
            'download_count': ['exact', 'lt', 'gt'],

            # BaseScoreModel values:
            'score': ['exact', 'lt', 'gt'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseTimestampModel values:
            'created': ['exact', 'lt', 'gt'],
            'updated': ['exact', 'lt', 'gt'],
        }
