# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class SportCategoryChoices(
    BaseIntegerToDictChoices,
):

    # Foot Sports
    RUNNING = 110, _('Running')
    HIKING = 120, _('Hiking')
    CLIMBING = 130, _('Climbing')
    VIA_FERRATA = 140, _('Via Ferrata')
    TRAIL_RUNNING = 150, _('Trail Running')

    # Winter Foot Sports
    WINTER_RUNNING = 210, _('Winter Running')
    WINTER_HIKING = 220, _('Winter Hiking')
    SNOWSHOEING = 230, _('Snowshoeing')
    SKI_TOURING = 240, _('Ski Touring')
    CROSS_COUNTRY_SKIING = 250, _('Cross-Country Skiing')

    # Cycling Sports
    BIKING = 301, _('Biking')
    MOUNTAIN_BIKING = 310, _('Mountain Biking')
    DOWNHILL_BIKING = 320, _('Downhill Biking')

    # Metadata class:
    class Meta:

        # Additional values translation:
        metadata = {
            110: {
                'icon': '🏃',
                'name': _('Running'),
                'description': _('Road and casual running')
            },
            120: {
                'icon': '🥾',
                'name': _('Hiking'),
                'description': _('Alpine and trail hiking')
            },
            130: {
                'icon': '🧗',
                'name': _('Climbing'),
                'description': _('Indoor and outdoor rock climbing')
            },
            140: {
                'icon': '🧗‍♂️',
                'name': _('Via Ferrata'),
                'description': _('Fixed-rope climbing routes')
            },
            150: {
                'icon': '🏞️',
                'name': _('Trail Running'),
                'description': _('Running on mountain or forest trails')
            },
            210: {
                'icon': '🏃❄️',
                'name': _('Winter Running'),
                'description': _('Running in winter conditions')
            },
            220: {
                'icon': '🥾❄️',
                'name': _('Winter Hiking'),
                'description': _('Snow-covered trail hiking')
            },
            230: {
                'icon': '🎿',
                'name': _('Snowshoeing'),
                'description': _('Walking with snowshoes')
            },
            240: {
                'icon': '⛷️',
                'name': _('Ski Touring'),
                'description': _('Backcountry uphill and downhill skiing')
            },
            250: {
                'icon': '🎿',
                'name': _('Cross-Country Skiing'),
                'description': _('Nordic skiing on prepared tracks')
            },
            310: {
                'icon': '🚴',
                'name': _('Biking'),
                'description': _('General biking on mixed terrains')
            },
            320: {
                'icon': '🚵',
                'name': _('Mountain Biking'),
                'description': _('Off-road and alpine biking')
            },
            330: {
                'icon': '🚵‍♂️⬇️',
                'name': _('Downhill Biking'),
                'description': _('Gravity downhill biking')
            }
        }
