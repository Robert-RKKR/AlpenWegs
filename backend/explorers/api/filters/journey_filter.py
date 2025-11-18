
# AlpenWegs application import:
from explorers.models.journey_model import JourneyModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Journey Model filter class:
class JourneyFilter(
    BaseFilter,
):

    class Meta:

        model = JourneyModel
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

            # BaseTimestampModel values:
            'created': ['exact', 'lt', 'gt'],
            'updated': ['exact', 'lt', 'gt'],

            # BaseDescriptiveModel values:
            'description': ['exact', 'icontains'],

            # BaseStatisticModel values:
            'comment_count': ['exact', 'lt', 'gt'],
            'visit_count': ['exact', 'lt', 'gt'],
            'download_count': ['exact', 'lt', 'gt'],

            # BaseMultiDayModel values:
            'start_date': ['exact', 'lt', 'gt'],
            'end_date': ['exact', 'lt', 'gt'],
            'total_days': ['exact', 'lt', 'gt'],
            'accommodation': ['exact'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseScoreModel values:
            'score': ['exact', 'lt', 'gt'],
        }
