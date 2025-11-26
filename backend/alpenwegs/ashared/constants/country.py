# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices


# Choices class:
class CountryChoices(
    BaseIntegerToDictChoices,
):

    # Choices values:
    SWITZERLAND = 41, 'Switzerland'
    GERMANY = 49, 'Germany'
    AUSTRIA = 43, 'Austria'
    FRANCE = 33, 'France'
    ITALY = 39, 'Italy'

# Module-level metadata dictionary:
COUNTRY_METADATA = {
    41: {
        'icon': '🇨🇭',
        'description': 'Alpine nation',
        'depend': None,
    },
    49: {
        'icon': '🇩🇪',
        'description': 'Neighbor to the north',
        'depend': None,
    },
    43: {
        'icon': '🇦🇹',
        'description': 'Eastern Alps',
        'depend': None,
    },
    33: {
        'icon': '🇫🇷',
        'description': 'Western neighbor',
        'depend': None,
    },
    39: {
        'icon': '🇮🇹',
        'description': 'Southern Alps',
        'depend': None,
    },
}
