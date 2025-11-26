# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices

# Accommodation Choices class:
class AccommodationTypeChoices(
    BaseIntegerToDictChoices,
):

    # Basic accommodation types:
    DORMITORY = 0, 'Dormitory'
    PRIVATE_ROOM = 1, 'Private Room'
    HOTEL = 2, 'Hotel'

    # Outdoor accommodation types:
    TENT = 10, 'Tent'
    CAMPING = 11, 'Camping Site'
    BIVOUAC = 12, 'Bivouac Spot'

    # Mountain-specific accommodation types:
    MOUNTAIN_HUT = 20, 'Mountain Hut'
    ALPINE_HUT = 21, 'Alpine Hut'
    WINTER_HUT = 22, 'Winter Hut'

    # Specialty / long-distance accommodation:
    HOSTEL = 30, 'Hostel'
    GUESTHOUSE = 31, 'Guesthouse'
    CABIN = 32, 'Cabin / Lodge'

    # Mixed or flexible:
    MIXED = 40, 'Mixed Accommodation'

ACCOMMODATION_TYPE_METADATA = {
    # Basic accommodation types:
    0: {
        'icon': '🛏️',
        'description': 'Shared sleeping space, usually multiple beds in one room.',
        'depend': None,
    },
    1: {
        'icon': '🚪',
        'description': 'Private room offering individual privacy and comfort.',
        'depend': None,
    },
    2: {
        'icon': '🏨',
        'description': 'Hotel accommodation with full comfort and services.',
        'depend': None,
    },

    # Outdoor accommodation types:
    10: {
        'icon': '⛺',
        'description': 'Personal tent setup in designated or wild locations.',
        'depend': None,
    },
    11: {
        'icon': '🏕️',
        'description': 'Camping site with facilities such as toilets or showers.',
        'depend': None,
    },
    12: {
        'icon': '🛖',
        'description': 'Minimalist bivouac spot for emergency or simple outdoor overnight stays.',
        'depend': None,
    },

    # Mountain-specific accommodation:
    20: {
        'icon': '🏚️',
        'description': 'Standard mountain hut offering shelter and basic services.',
        'depend': None,
    },
    21: {
        'icon': '🏔️',
        'description': 'Alpine hut for high-altitude stays, often with limited facilities.',
        'depend': None,
    },
    22: {
        'icon': '❄️',
        'description': 'Winter hut open during cold seasons, usually basic and self-service.',
        'depend': None,
    },

    # Specialty / long-distance accommodation:
    30: {
        'icon': '🛌',
        'description': 'Hostel accommodation ideal for long-distance travelers.',
        'depend': None,
    },
    31: {
        'icon': '🏡',
        'description': 'Guesthouse offering homely stays with local atmosphere.',
        'depend': None,
    },
    32: {
        'icon': '🪵',
        'description': 'Cabin or lodge providing rustic and cosy accommodation.',
        'depend': None,
    },

    # Mixed or flexible:
    40: {
        'icon': '🔀',
        'description': 'Flexible accommodation combining multiple types.',
        'depend': None,
    },
}
