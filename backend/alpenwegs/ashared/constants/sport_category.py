# AlpenWeg import:
from alpenwegs.ashared.constants.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class SportCategoryChoices(
    BaseIntegerChoices,
):

    # Foot Sports
    RUNNING = 101, _('Running')
    HIKING = 102, _('Hiking')
    CLIMBING = 104, _('Climbing')
    VIA_FERRATA = 105, _('Via Ferrata')
    TRAIL_RUNNING = 107, _('Trail Running')

    # Winter Foot Sports
    WINTER_RUNNING = 201, _('Winter Running')
    WINTER_HIKING = 202, _('Winter Hiking')
    SNOWSHOEING = 205, _('Snowshoeing')
    SKI_TOURING = 206, _('Ski Touring')
    CROSS_COUNTRY_SKIING = 207, _('Cross-Country Skiing')

    # Cycling Sports
    BIKING = 301, _('Biking')
    MOUNTAIN_BIKING = 302, _('Mountain Biking')
    DOWNHILL_BIKING = 303, _('Downhill Biking')


# Additional values translation:
SPORT_CATEGORY_METADATA = {
    SportCategoryChoices.RUNNING: {
        'icon': '🏃',
        'name': _('Running'),
        'description': _('Road and casual running')
    },
    SportCategoryChoices.HIKING: {
        'icon': '🥾',
        'name': _('Hiking'),
        'description': _('Alpine and trail hiking')
    },
    SportCategoryChoices.CLIMBING: {
        'icon': '🧗',
        'name': _('Climbing'),
        'description': _('Indoor and outdoor rock climbing')
    },
    SportCategoryChoices.VIA_FERRATA: {
        'icon': '🧗‍♂️',
        'name': _('Via Ferrata'),
        'description': _('Fixed-rope climbing routes')
    },
    SportCategoryChoices.TRAIL_RUNNING: {
        'icon': '🏞️',
        'name': _('Trail Running'),
        'description': _('Running on mountain or forest trails')
    },
    SportCategoryChoices.WINTER_RUNNING: {
        'icon': '🏃❄️',
        'name': _('Winter Running'),
        'description': _('Running in winter conditions')
    },
    SportCategoryChoices.WINTER_HIKING: {
        'icon': '🥾❄️',
        'name': _('Winter Hiking'),
        'description': _('Snow-covered trail hiking')
    },
    SportCategoryChoices.SNOWSHOEING: {
        'icon': '🎿',
        'name': _('Snowshoeing'),
        'description': _('Walking with snowshoes')
    },
    SportCategoryChoices.SKI_TOURING: {
        'icon': '⛷️',
        'name': _('Ski Touring'),
        'description': _('Backcountry uphill and downhill skiing')
    },
    SportCategoryChoices.CROSS_COUNTRY_SKIING: {
        'icon': '🎿',
        'name': _('Cross-Country Skiing'),
        'description': _('Nordic skiing on prepared tracks')
    },
    SportCategoryChoices.BIKING: {
        'icon': '🚴',
        'name': _('Biking'),
        'description': _('General biking on mixed terrains')
    },
    SportCategoryChoices.MOUNTAIN_BIKING: {
        'icon': '🚵',
        'name': _('Mountain Biking'),
        'description': _('Off-road and alpine biking')
    },
    SportCategoryChoices.DOWNHILL_BIKING: {
        'icon': '🚵‍♂️⬇️',
        'name': _('Downhill Biking'),
        'description': _('Gravity downhill biking')
    }
}
