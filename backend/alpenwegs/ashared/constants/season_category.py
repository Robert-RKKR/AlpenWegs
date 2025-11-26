# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices


# Month choices class:
class MonthChoices(
    BaseIntegerToDictChoices,
):

    JANUARY = 1, 'January'
    FEBRUARY = 2, 'February'
    MARCH = 3, 'March'
    APRIL = 4, 'April'
    MAY = 5, 'May'
    JUNE = 6, 'June'
    JULY = 7, 'July'
    AUGUST = 8, 'August'
    SEPTEMBER = 9, 'September'
    OCTOBER = 10, 'October'
    NOVEMBER = 11, 'November'
    DECEMBER = 12, 'December'

# Module-level metadata dictionary:
MONTH_METADATA =  {
    1: {
        'icon': '❄️',
        'description': 'Winter month, cold and snowy in the Alps',
        'depend': None,
    },
    2: {
        'icon': '⛷️',
        'description': 'Peak of ski season in Switzerland',
        'depend': None,
    },
    3: {
        'icon': '🌱',
        'description': 'Beginning of spring in lower valleys',
        'depend': None,
    },
    4: {
        'icon': '🌸',
        'description': 'Spring blossoms, still snow in mountains',
        'depend': None,
    },
    5: {
        'icon': '🌼',
        'description': 'Warm spring, hiking starts in lower areas',
        'depend': None,
    },
    6: {
        'icon': '☀️',
        'description': 'Start of summer hiking season',
        'depend': None,
    },
    7: {
        'icon': '🏞️',
        'description': 'Summer, ideal for alpine adventures',
        'depend': None,
    },
    8: {
        'icon': '🚵',
        'description': 'Peak outdoor activity season in the Alps',
        'depend': None,
    },
    9: {
        'icon': '🍂',
        'display': 'September',
        'description': 'Start of autumn, cooler hiking conditions',
        'depend': None,
    },
    10: {
        'icon': '🎃',
        'description': 'Autumn colors, some early snow in high Alps',
        'depend': None,
    },
    11: {
        'icon': '🍁',
        'display': 'November',
        'description': 'Transition to winter, foggy valleys',
        'depend': None,
    },
    12: {
        'icon': '🎄',
        'description': 'Winter begins, ski season opens',
        'depend': None,
    },
}


# Season choices class:
class SeasonChoices(
    BaseIntegerToDictChoices,
):

    WINTER = 1, 'Winter'
    SPRING = 2, 'Spring'
    SUMMER = 3, 'Summer'
    AUTUMN = 4, 'Autumn'

# Module-level metadata dictionary:
SEASON_METADATA =  {
    1: {
        'icon': '❄️',
        'description': 'Snow season, skiing and winter sports'
    },
    2: {
        'icon': '🌸',
        'description': 'Blooming season, hiking starts in valleys',
        'depend': None,
    },
    3: {
        'icon': '☀️',
        'description': 'Peak outdoor season, alpine hiking and biking',
        'depend': None,
    },
    4: {
        'icon': '🍂',
        'description': 'Colorful landscapes, cooler hiking conditions',
        'depend': None,
    },
}
