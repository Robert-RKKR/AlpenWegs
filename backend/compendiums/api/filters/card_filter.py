# AlpenWegs application import:
from compendiums.models.card_model import CardModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Card Model filter class:
class CardFilter(
    BaseFilter,
):

    class Meta:

        model = CardModel
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

            # CardModel values:
            'poi': ['exact'],
            'elevation': ['exact', 'lt', 'gt'],
            'type': ['exact'],
            'category': ['exact'],
            'category_specific_difficulty': ['exact'],
        }
