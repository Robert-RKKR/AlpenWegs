# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices


# Choices class:
class RegionTypeChoices(
    BaseIntegerToDictChoices,
):
    """
    Defines logical region types used across AlpenWeg.
    Covers administrative, geographic, and natural regions.
    """

    # Administrative regions:
    CANTON = 2, 'Canton'
    DISTRICT = 3, 'District'
    MUNICIPALITY = 4, 'Municipality'

    # Geographic regions (human-defined):
    GEOGRAPHIC_REGION = 10, 'Geographic region'
    CULTURAL_REGION = 11, 'Cultural region'
    TOURISM_REGION = 12, 'Tourism region'

    # Natural regions (nature-defined):
    NATURAL_REGION = 20, 'Natural region'
    MOUNTAIN_RANGE = 21, 'Mountain range'
    VALLEY = 22, 'Valley'
    PLATEAU = 23, 'Plateau'
    LAKE_REGION = 24, 'Lake region'
    RIVER_BASIN = 25, 'River basin'

    # Special / abstract:
    SPECIAL_REGION = 99, 'Special region'

# Module-level metadata dictionary:
REGION_TYPE_METADATA = {
    2: {
        'icon': '🛡️',
        'description': 'Swiss canton or equivalent federal region.',
        'depend': 1,
        'category': 'administrative',
    },
    3: {
        'icon': '📍',
        'description': 'Administrative district within a canton.',
        'depend': 2,
        'category': 'administrative',
    },
    4: {
        'icon': '🏘️',
        'description': 'Municipality, town, or city.',
        'depend': 3,
        'category': 'administrative',
    },
    10: {
        'icon': '🗺️',
        'description': 'Broad geographic region (e.g. Central Switzerland).',
        'depend': 1,
        'category': 'geographic',
    },
    11: {
        'icon': '🏛️',
        'description': 'Region defined by shared culture or history.',
        'depend': None,
        'category': 'geographic',
    },
    12: {
        'icon': '🎒',
        'description': 'Tourism-oriented region used for travel and hiking.',
        'depend': None,
        'category': 'geographic',
    },
    20: {
        'icon': '🌿',
        'description': 'Naturally defined region (flora, fauna, geology).',
        'depend': None,
        'category': 'natural',
    },
    21: {
        'icon': '⛰️',
        'description': 'Mountain range consisting of multiple peaks.',
        'depend': 20,
        'category': 'natural',
    },
    22: {
        'icon': '🏞️',
        'description': 'Valley shaped by glaciers or rivers.',
        'depend': 20,
        'category': 'natural',
    },
    23: {
        'icon': '🟫',
        'description': 'Highland or plateau region.',
        'depend': 20,
        'category': 'natural',
    },
    24: {
        'icon': '💧',
        'description': 'Region dominated by lakes or lake systems.',
        'depend': 20,
        'category': 'natural',
    },
    25: {
        'icon': '🌊',
        'description': 'Hydrological basin of a river system.',
        'depend': 20,
        'category': 'natural',
    },
    99: {
        'icon': '⭐',
        'description': 'Special or abstract region (events, challenges, lore).',
        'depend': None,
        'category': 'special',
    },
}
