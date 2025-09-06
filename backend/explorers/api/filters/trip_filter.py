# AlpenWegs application import:
from explorers.models.trip_model import TripModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Trip Model filter class:
class TripFilter(
    BaseFilter,
):

    class Meta:

        model = TripModel
        fields = {
            # BaseModel values:
            'id': ['exact'],

            # BaseIdentificationModel values:
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'snippet': ['exact', 'icontains'],

            # BaseDescriptiveModel values:
            'description': ['exact', 'icontains'],

            # BaseSportCategoryModel values:
            'category': ['exact'],
            'category_specific_difficulty': ['exact'],

            # TripModel values:
            'days': ['exact', 'lt', 'gt'],

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
