# AlpenWeg import:
from alpenwegs.ashared.constants.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class PoiCategoryChoices(
    BaseIntegerChoices,
):

    # Choices values:
    CITY = 1, 'City'
    VILLAGE = 2, 'Village'
    HUT = 3, 'Mountain Hut'
    PEAK = 4, 'Mountain Peak'
    LAKE = 5, 'Lake'
    RIVER = 6, 'River'
    PASS = 7, 'Mountain Pass'
    FOREST = 8, 'Forest Area'
    GLACIER = 9, 'Glacier'
    OTHER = 10, 'Other'
