# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Month choices class:
class MonthChoices(
    BaseIntegerToDictChoices,
):

    JANUARY = 1, _('January')
    FEBRUARY = 2, _('February')
    MARCH = 3, _('March')
    APRIL = 4, _('April')
    MAY = 5, _('May')
    JUNE = 6, _('June')
    JULY = 7, _('July')
    AUGUST = 8, _('August')
    SEPTEMBER = 9, _('September')
    OCTOBER = 10, _('October')
    NOVEMBER = 11, _('November')
    DECEMBER = 12, _('December')

    # Metadata class:
    class Meta:

        metadata = {
            1: {
                'icon': '❄️',
                'name': _('January'),
                'description': _('Winter month, cold and snowy in the Alps')
            },
            2: {
                'icon': '⛷️',
                'name': _('February'),
                'description': _('Peak of ski season in Switzerland')
            },
            3: {
                'icon': '🌱',
                'name': _('March'),
                'description': _('Beginning of spring in lower valleys')
            },
            4: {
                'icon': '🌸',
                'name': _('April'),
                'description': _('Spring blossoms, still snow in mountains')
            },
            5: {
                'icon': '🌼',
                'name': _('May'),
                'description': _('Warm spring, hiking starts in lower areas')
            },
            6: {
                'icon': '☀️',
                'name': _('June'),
                'description': _('Start of summer hiking season')
            },
            7: {
                'icon': '🏞️',
                'name': _('July'),
                'description': _('Summer, ideal for alpine adventures')
            },
            8: {
                'icon': '🚵',
                'name': _('August'),
                'description': _('Peak outdoor activity season in the Alps')
            },
            9: {
                'icon': '🍂',
                'name': _('September'),
                'description': _('Start of autumn, cooler hiking conditions')
            },
            10: {
                'icon': '🎃',
                'name': _('October'),
                'description': _('Autumn colors, some early snow in high Alps')
            },
            11: {
                'icon': '🍁',
                'name': _('November'),
                'description': _('Transition to winter, foggy valleys')
            },
            12: {
                'icon': '🎄',
                'name': _('December'),
                'description': _('Winter begins, ski season opens')
            }
        }


# Season choices class:
class SeasonChoices(
    BaseIntegerToDictChoices,
):

    WINTER = 1, _('Winter')
    SPRING = 2, _('Spring')
    SUMMER = 3, _('Summer')
    AUTUMN = 4, _('Autumn')

    # Metadata class:
    class Meta:

        metadata = {
            1: {
                'icon': '❄️',
                'name': _('Winter'),
                'description': _('Snow season, skiing and winter sports')
            },
            2: {
                'icon': '🌸',
                'name': _('Spring'),
                'description': _('Blooming season, hiking starts in valleys')
            },
            3: {
                'icon': '☀️',
                'name': _('Summer'),
                'description': _('Peak outdoor season, alpine hiking and biking')
            },
            4: {
                'icon': '🍂',
                'name': _('Autumn'),
                'description': _('Colorful landscapes, cooler hiking conditions')
            }
        }
