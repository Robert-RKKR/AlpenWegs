# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices

# Choices class:
class SportCategoryChoices(
    BaseIntegerToDictChoices,
):

    # Foot Sports
    RUNNING = 110, 'Running'
    HIKING = 120, 'Hiking'
    CLIMBING = 130, 'Climbing'
    VIA_FERRATA = 140, 'Via Ferrata'
    TRAIL_RUNNING = 150, 'Trail Running'

    # Winter Foot Sports
    WINTER_RUNNING = 210, 'Winter Running'
    WINTER_HIKING = 220, 'Winter Hiking'
    SNOWSHOEING = 230, 'Snowshoeing'
    SKI_TOURING = 240, 'Ski Touring'
    CROSS_COUNTRY_SKIING = 250, 'Cross-Country Skiing'

    # Cycling Sports
    BIKING = 301, 'Biking'
    MOUNTAIN_BIKING = 310, 'Mountain Biking'
    DOWNHILL_BIKING = 320, 'Downhill Biking'

# Module-level metadata dictionary:
SPORT_CATEGORY_METADATA =  {
    110: {
        'icon': '🏃',
        'description': 'Road and casual running',
        'depend': None,
    },
    120: {
        'icon': '🥾',
        'description': 'Alpine and trail hiking',
        'depend': None,
    },
    130: {
        'icon': '🧗',
        'description': 'Indoor and outdoor rock climbing',
        'depend': None,
    },
    140: {
        'icon': '🧗‍♂️',
        'description': 'Fixed-rope climbing routes',
        'depend': None,
    },
    150: {
        'icon': '🏞️',
        'description': 'Running on mountain or forest trails',
        'depend': None,
    },
    210: {
        'icon': '🏃❄️',
        'description': 'Running in winter conditions',
        'depend': None,
    },
    220: {
        'icon': '🥾❄️',
        'description': 'Snow-covered trail hiking',
        'depend': None,
    },
    230: {
        'icon': '🎿',
        'description': 'Walking with snowshoes',
        'depend': None,
    },
    240: {
        'icon': '⛷️',
        'description': 'Back country uphill and downhill skiing',
        'depend': None,
    },
    250: {
        'icon': '🎿',
        'description': 'Nordic skiing on prepared tracks',
        'depend': None,
    },
    310: {
        'icon': '🚴',
        'description': 'General biking on mixed terrains',
        'depend': None,
    },
    320: {
        'icon': '🚵',
        'description': 'Off-road and alpine biking',
        'depend': None,
    },
    330: {
        'icon': '🚵‍♂️⬇️',
        'description': 'Gravity downhill biking',
        'depend': None,
    },
}
