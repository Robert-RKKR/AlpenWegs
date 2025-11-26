# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices


# Choices class:
class PoiCategoryChoices(
    BaseIntegerToDictChoices,
):

    # Mountains POIs types:
    PEAK = 1, 'Peak'
    RANGE = 2, 'Range'
    HUT = 3, 'Hut'
    ROUTE = 4, 'Route'
    BRIDGE = 5, 'Bridge'
    PASS = 6, 'Pass'
    TRAIL = 7, 'Trail'
    LAKE = 8, 'Lake'
    CAVE = 9, 'Cave'
    RUINS = 10, 'Ruins'
    GLACIER = 11, 'Glacier'
    CABLE_CAR = 12, 'Cable Car Station'

    # City POIs types:
    CITY = 21, 'City'
    VILLAGE = 22, 'Village'
    TRAIN_STATION = 23, 'Train Station'
    PARKING_SPACE = 24, 'Parking Space'
    RESTAURANT = 25, 'Restaurant'
    BAR = 26, 'Bar'
    ACCOMMODATION = 27, 'Accommodation'
    TOURIST_INFO = 28, 'Tourist Information'

    # Organizational POIs types:
    GEMAINDE = 41, 'Gemeinde'
    CANTON = 42, 'Canton'

    # Other POIs types:
    OTHER = 99, 'Other'

# Module-level metadata dictionary:
POI_CATEGORY_METADATA = {
    # Mountains POIs types:
    1: {
        'icon': '🏔️',
        'description': 'A mountain peak or summit.',
        'depend': None,
    },
    2: {
        'icon': '⛰️',
        'description': 'A mountain range containing multiple peaks.',
        'depend': None,
    },
    3: {
        'icon': '🏚️',
        'description': 'A mountain hut or alpine shelter.',
        'depend': None,
    },
    4: {
        'icon': '🗺️',
        'description': 'A designated mountain route or hiking line.',
        'depend': None,
    },
    5: {
        'icon': '🌉',
        'description': 'A bridge located in mountain or valley terrain.',
        'depend': None,
    },
    6: {
        'icon': '🛤️',
        'description': 'A mountain pass connecting valleys or regions.',
        'depend': None,
    },
    7: {
        'icon': '🥾',
        'description': 'A marked hiking or mountain trail.',
        'depend': None,
    },
    8: {
        'icon': '🏞️',
        'description': 'A natural mountain lake or alpine water body.',
        'depend': None,
    },
    9: {
        'icon': '🕳️',
        'description': 'A mountain cave or natural cavern.',
        'depend': None,
    },
    10: {
        'icon': '🏚️🪨',
        'description': 'Ruins or historical remains found in mountain areas.',
        'depend': None,
    },
    11: {
        'icon': '🧊',
        'description': 'A glacier or permanent snow/ice structure.',
        'depend': None,
    },
    12: {
        'icon': '🚡',
        'description': 'Cable car, gondola, or mountain lift station.',
        'depend': None,
    },

    # City POIs types:
    21: {
        'icon': '🌆',
        'description': 'A city-level point of interest.',
        'depend': None,
    },
    22: {
        'icon': '🏘️',
        'description': 'A village or smaller settlement.',
        'depend': None,
    },
    23: {
        'icon': '🚆',
        'description': 'A train station or rail access point.',
        'depend': None,
    },
    24: {
        'icon': '🅿️',
        'description': 'A parking area or designated parking zone.',
        'depend': None,
    },
    25: {
        'icon': '🍽️',
        'description': 'A restaurant or dining place.',
        'depend': None,
    },
    26: {
        'icon': '🍻',
        'description': 'A bar, pub, or beverage establishment.',
        'depend': None,
    },
    27: {
        'icon': '🏨',
        'description': 'Accommodation such as hotel, guesthouse, or lodge.',
        'depend': None,
    },
    28: {
        'icon': 'ℹ️',
        'description': 'Tourist information office or visitor center.',
        'depend': None,
    },

    # Organizational POIs types:
    41: {
        'icon': '🏢',
        'description': 'Gemeinde / municipal administration.',
        'depend': None,
    },
    42: {
        'icon': '🏛️',
        'description': 'Canton-level administrative or official location.',
        'depend': None,
    },

    # Other POIs types:
    99: {
        'icon': '📍',
        'description': 'Other point of interest not categorized elsewhere.',
        'depend': None,
    },
}
