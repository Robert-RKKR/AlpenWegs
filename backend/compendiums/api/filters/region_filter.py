# AlpenWegs application import:
from compendiums.models.region_model import RegionModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Region Model filter class:
class RegionFilter(
    BaseFilter,
):

    class Meta:

        model = RegionModel
        fields = {
            # BaseModel values:
            'id': ['exact'],

            # BaseIdentificationModel values:
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'snippet': ['exact', 'icontains'],

            # BaseDescriptiveModel values:
            'description': ['exact', 'icontains'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseTimestampModel values:
            'created': ['exact', 'lt', 'gt'],
            'updated': ['exact', 'lt', 'gt'],

            # RegionModel values:
            'country': ['exact'],
        }
