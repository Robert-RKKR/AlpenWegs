# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class CountryChoices(
    BaseIntegerToDictChoices,
):

    # Choices values:
    SWITZERLAND = 41, _('Switzerland')
    GERMANY = 49, _('Germany')
    AUSTRIA = 43, _('Austria')
    FRANCE = 33, _('France')
    ITALY = 39, _('Italy')

    # Metadata class:
    class Meta:

        # Additional values translation:
        metadata = {
            41: {
                'icon': '🇨🇭',
                'name': _('Switzerland'),
                'description': _('Alpine nation'),
            },
            49: {
                'icon': '🇩🇪',
                'name': _('Germany'),
                'description': _('Neighbor to the north'),
            },
            43: {
                'icon': '🇦🇹',
                'name': _('Austria'),
                'description': _('Eastern Alps')
            },
            33: {
                'icon': '🇫🇷',
                'name': _('France'),
                'description': _('Western neighbor')
            },
            39: {
                'icon': '🇮🇹',
                'name': _('Italy'),
                'description': _('Southern Alps')
            }
        }
