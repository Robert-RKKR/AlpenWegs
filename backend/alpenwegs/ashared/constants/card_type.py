# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices


# Choices class:
class CardTypeChoices(
    BaseIntegerToDictChoices,
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

# Module-level metadata dictionary:
CARD_TYPE_METADATA = {
    1: {
        'icon': '🏔️',
        'description': 'A mountain peak or summit.',
        'depend': None,
    },
    2: {
        'icon': '⛰️',
        'description': 'A mountain range consisting of multiple peaks.',
        'depend': None,
    },
    3: {
        'icon': '🏚️',
        'description': 'A mountain hut or alpine shelter.',
        'depend': None,
    },
    4: {
        'icon': '🗺️',
        'description': 'A mountain route or hiking path.',
        'depend': None,
    },
    5: {
        'icon': '🌉',
        'description': 'A bridge located in alpine or mountainous terrain.',
        'depend': None,
    },
    6: {
        'icon': '🛤️',
        'description': 'A mountain pass connecting two valleys or regions.',
        'depend': None,
    },
    7: {
        'icon': '🥾',
        'description': 'A hiking trail or marked mountain path.',
        'depend': None,
    },
    8: {
        'icon': '🏞️',
        'description': 'A mountain lake or alpine water body.',
        'depend': None,
    },
    9: {
        'icon': '🕳️',
        'description': 'A mountain cave or cavern.',
        'depend': None,
    },
    10: {
        'icon': '🏚️',
        'description': 'Ruins or old structures found in the mountains.',
        'depend': None,
    },
    99: {
        'icon': '⭐',
        'description': 'Special card with unique meaning or conditions.',
        'depend': None,
    },
}
