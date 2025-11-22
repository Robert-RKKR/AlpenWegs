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

    # # Metadata class:
    # class Meta:

    #     metadata = {
    #         1: {
    #             'icon': '❄️',
    #             'name': 'January',
    #             'description': 'Winter month, cold and snowy in the Alps',
    #         },
    #         2: {
    #             'icon': '⛷️',
    #             'name': 'February',
    #             'description': 'Peak of ski season in Switzerland',
    #         },
    #         3: {
    #             'icon': '🌱',
    #             'name': 'March',
    #             'description': 'Beginning of spring in lower valleys',
    #         },
    #         4: {
    #             'icon': '🌸',
    #             'name': 'April',
    #             'description': 'Spring blossoms, still snow in mountains',
    #         },
    #         5: {
    #             'icon': '🌼',
    #             'name': 'May',
    #             'description': 'Warm spring, hiking starts in lower areas',
    #         },
    #         6: {
    #             'icon': '☀️',
    #             'name': 'June',
    #             'description': 'Start of summer hiking season',
    #         },
    #         7: {
    #             'icon': '🏞️',
    #             'name': 'July',
    #             'description': 'Summer, ideal for alpine adventures',
    #         },
    #         8: {
    #             'icon': '🚵',
    #             'name': 'August',
    #             'description': 'Peak outdoor activity season in the Alps',
    #         },
    #         9: {
    #             'icon': '🍂',
    #             'name': 'September',
    #             'description': 'Start of autumn, cooler hiking conditions',
    #         },
    #         10: {
    #             'icon': '🎃',
    #             'name': 'October',
    #             'description': 'Autumn colors, some early snow in high Alps',
    #         },
    #         11: {
    #             'icon': '🍁',
    #             'name': 'November',
    #             'description': 'Transition to winter, foggy valleys',
    #         },
    #         12: {
    #             'icon': '🎄',
    #             'name': 'December',
    #             'description': 'Winter begins, ski season opens',
    #         }
    #     }


# Season choices class:
class SeasonChoices(
    BaseIntegerToDictChoices,
):

    WINTER = 1, 'Winter'
    SPRING = 2, 'Spring'
    SUMMER = 3, 'Summer'
    AUTUMN = 4, 'Autumn'

    # # Metadata class:
    # class Meta:

    #     metadata = {
    #         1: {
    #             'icon': '❄️',
    #             'name': 'Winter',
    #             'description': 'Snow season, skiing and winter sports'
    #         },
    #         2: {
    #             'icon': '🌸',
    #             'name': 'Spring',
    #             'description': 'Blooming season, hiking starts in valleys',
    #         },
    #         3: {
    #             'icon': '☀️',
    #             'name': 'Summer',
    #             'description': 'Peak outdoor season, alpine hiking and biking',
    #         },
    #         4: {
    #             'icon': '🍂',
    #             'name': 'Autumn',
    #             'description': 'Colorful landscapes, cooler hiking conditions',
    #         }
    #     }
