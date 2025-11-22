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

    # # Metadata class:
    # class Meta:

    #     # Additional values translation:
    #     metadata = {
    #         110: {
    #             'icon': '🏃',
    #             'name': 'Running',
    #             'description': 'Road and casual running',
    #         },
    #         120: {
    #             'icon': '🥾',
    #             'name': 'Hiking',
    #             'description': 'Alpine and trail hiking',
    #         },
    #         130: {
    #             'icon': '🧗',
    #             'name': 'Climbing',
    #             'description': 'Indoor and outdoor rock climbing',
    #         },
    #         140: {
    #             'icon': '🧗‍♂️',
    #             'name': 'Via Ferrata',
    #             'description': 'Fixed-rope climbing routes',
    #         },
    #         150: {
    #             'icon': '🏞️',
    #             'name': 'Trail Running',
    #             'description': 'Running on mountain or forest trails',
    #         },
    #         210: {
    #             'icon': '🏃❄️',
    #             'name': 'Winter Running',
    #             'description': 'Running in winter conditions',
    #         },
    #         220: {
    #             'icon': '🥾❄️',
    #             'name': 'Winter Hiking',
    #             'description': 'Snow-covered trail hiking',
    #         },
    #         230: {
    #             'icon': '🎿',
    #             'name': 'Snowshoeing',
    #             'description': 'Walking with snowshoes',
    #         },
    #         240: {
    #             'icon': '⛷️',
    #             'name': 'Ski Touring',
    #             'description': 'Backcountry uphill and downhill skiing',
    #         },
    #         250: {
    #             'icon': '🎿',
    #             'name': 'Cross-Country Skiing',
    #             'description': 'Nordic skiing on prepared tracks',
    #         },
    #         310: {
    #             'icon': '🚴',
    #             'name': 'Biking',
    #             'description': 'General biking on mixed terrains',
    #         },
    #         320: {
    #             'icon': '🚵',
    #             'name': 'Mountain Biking',
    #             'description': 'Off-road and alpine biking',
    #         },
    #         330: {
    #             'icon': '🚵‍♂️⬇️',
    #             'name': 'Downhill Biking',
    #             'description': 'Gravity downhill biking',
    #         }
    #     }
