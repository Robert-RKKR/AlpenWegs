# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerChoices


# Choices class:
class CardTypeChoices(
    BaseIntegerChoices,
):

    # Choices values:
    MOUNTAIN_PEAK = 1, 'Mountain peak'
    MOUNTAIN_RANGE = 2, 'Mountain range'
    MOUNTAIN_HUT = 3, 'Mountain hut'
    MOUNTAIN_ROUTE = 4, 'Mountain route'
    MOUNTAIN_BRIDGE = 5, 'Mountain bridge'
    MOUNTAIN_PASS = 6, 'Mountain pass'
    MOUNTAIN_TRAIL = 7, 'Mountain trail'
    MOUNTAIN_LAKE = 8, 'Mountain lake'
    MOUNTAIN_CAVE = 9, 'Mountain cave'
    MOUNTAIN_RUINS = 10, 'Mountain ruins'
    SPECIAL_CARD = 99, 'Special card'
