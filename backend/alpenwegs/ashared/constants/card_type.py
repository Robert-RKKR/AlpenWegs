# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class CardTypeChoices(
    BaseIntegerChoices,
):

    # Choices values:
    MOUNTAIN_PEAK = 1, _('Mountain peak')
    MOUNTAIN_RANGE = 2, _('Mountain range')
    MOUNTAIN_HUT = 3, _('Mountain hut')
    MOUNTAIN_ROUTE = 4, _('Mountain route')
    MOUNTAIN_BRIDGE = 5, _('Mountain bridge')
    MOUNTAIN_PASS = 6, _('Mountain pass')
    MOUNTAIN_TRAIL = 7, _('Mountain trail')
    MOUNTAIN_LAKE = 8, _('Mountain lake')
    MOUNTAIN_CAVE = 9, _('Mountain cave')
    MOUNTAIN_RUINS = 10, _('Mountain ruins')
    SPECIAL_CARD = 99, _('Special card')
