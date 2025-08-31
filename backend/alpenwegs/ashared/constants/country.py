# AlpenWeg import:
from alpenwegs.ashared.constants.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class CountryChoices(
    BaseIntegerChoices,
):

    # Choices values:
    SWITZERLAND = 41, _('Switzerland')
    GERMANY = 49, _('Germany')
    AUSTRIA = 43, _('Austria')
    FRANCE = 33, _('France')
    ITALY = 39, _('Italy')


# Additional values translation:
COUNTRY_METADATA = {
    CountryChoices.SWITZERLAND: {
        'icon': '🇨🇭',
        'name': _('Switzerland'),
        'description': _('Alpine nation'),
    },
    CountryChoices.GERMANY: {
        'icon': '🇩🇪',
        'name': _('Germany'),
        'description': _('Neighbor to the north'),
    },
    CountryChoices.AUSTRIA: {
        'icon': '🇦🇹',
        'name': _('Austria'),
        'description': _('Eastern Alps')
    },
    CountryChoices.FRANCE: {
        'icon': '🇫🇷',
        'name': _('France'),
        'description': _('Western neighbor')
    },
    CountryChoices.ITALY: {
        'icon': '🇮🇹',
        'name': _('Italy'),
        'description': _('Southern Alps')
    }
}
