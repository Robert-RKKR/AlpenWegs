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
        'name': 'Switzerland',
        'description': 'Alpine nation',
    },
    49: {
        'icon': '🇩🇪',
        'name': 'Germany',
        'description': 'Neighbor to the north',
    },
    43: {
        'icon': '🇦🇹',
        'name': 'Austria',
        'description': 'Eastern Alps',
    },
    33: {
        'icon': '🇫🇷',
        'name': 'France',
        'description': 'Western neighbor',
    },
    39: {
        'icon': '🇮🇹',
        'name': 'Italy',
        'description': 'Southern Alps',
    },
}
