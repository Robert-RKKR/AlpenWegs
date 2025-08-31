# AlpenWeg import:
from alpenwegs.ashared.constants.sport_category import SportCategoryChoices
from alpenwegs.ashared.constants.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class SportCategoryDifficultyChoices(
    BaseIntegerChoices,
):

    # Hiking Difficulty:
    T1 = 121, _('T1 - Easy Hiking')
    T2 = 122, _('T2 - Mountain Hiking')
    T3 = 123, _('T3 - Demanding Mountain Hiking')
    T4 = 124, _('T4 - Alpine Hiking')
    T5 = 125, _('T5 - Demanding Alpine Hiking')
    T6 = 126, _('T6 - Difficult Alpine Hiking')

    # Via Ferrata Difficulty
    K1 = 141, _('K1 - Easy')
    K2 = 142, _('K2 - Moderate')
    K3 = 143, _('K3 - Difficult')
    K4 = 144, _('K4 - Very Difficult')
    K5 = 145, _('K5 - Extreme')
    K6 = 146, _('K6 - Expert')

    # Climbing Difficulty:
    III = 131, _('UIAA III')
    IV = 132, _('UIAA IV')
    V = 133, _('UIAA V')
    VI = 134, _('UIAA VI')
    VII = 135, _('UIAA VII')


# Additional values translation:
SPORT_CATEGORY_DIFFICULTY_METADATA = {
    # Hiking T-scale
    SportCategoryDifficultyChoices.T1: {
        'icon': '🥾',
        'name': _('T1 - Easy Hiking'),
        'description': _('Simple paths, well-marked, minimal risk.'),
        'sport_category': SportCategoryChoices.HIKING,
    },
    SportCategoryDifficultyChoices.T2: {
        'icon': '🥾',
        'name': _('T2 - Mountain Hiking'),
        'description': _('Mountain trails, more uneven ground, moderate risk.'),
        'sport_category': SportCategoryChoices.HIKING,
    },
    SportCategoryDifficultyChoices.T3: {
        'icon': '🥾',
        'name': _('T3 - Demanding Mountain Hiking'),
        'description': _('Exposed sections, need for surefootedness, some hands.'),
        'sport_category': SportCategoryChoices.HIKING,
    },
    SportCategoryDifficultyChoices.T4: {
        'icon': '🥾',
        'name': _('T4 - Alpine Hiking'),
        'description': _('Steeper terrain, occasional use of hands, high exposure.'),
        'sport_category': SportCategoryChoices.HIKING,
    },
    SportCategoryDifficultyChoices.T5: {
        'icon': '🥾',
        'name': _('T5 - Demanding Alpine Hiking'),
        'description': _('Very exposed, poor paths, need alpine experience.'),
        'sport_category': SportCategoryChoices.HIKING,
    },
    SportCategoryDifficultyChoices.T6: {
        'icon': '🥾',
        'name': _('T6 - Difficult Alpine Hiking'),
        'description': _('Exposed climbing terrain, dangerous, expert level.'),
        'sport_category': SportCategoryChoices.HIKING,
    },

    # Via Ferrata K-scale
    SportCategoryDifficultyChoices.K1: {
        'icon': '🧗‍♂️',
        'name': _('K1 - Easy'),
        'description': _('Beginner ferrata, short ladders, well-protected.'),
        'sport_category': SportCategoryChoices.VIA_FERRATA,
    },
    SportCategoryDifficultyChoices.K2: {
        'icon': '🧗‍♂️',
        'name': _('K2 - Moderate'),
        'description': _('Moderate climbing, some exposure.'),
        'sport_category': SportCategoryChoices.VIA_FERRATA,
    },
    SportCategoryDifficultyChoices.K3: {
        'icon': '🧗‍♂️',
        'name': _('K3 - Difficult'),
        'description': _('Steeper sections, higher exposure.'),
        'sport_category': SportCategoryChoices.VIA_FERRATA,
    },
    SportCategoryDifficultyChoices.K4: {
        'icon': '🧗‍♂️',
        'name': _('K4 - Very Difficult'),
        'description': _('Athletic climbing, vertical or overhanging.'),
        'sport_category': SportCategoryChoices.VIA_FERRATA,
    },
    SportCategoryDifficultyChoices.K5: {
        'icon': '🧗‍♂️',
        'name': _('K5 - Extreme'),
        'description': _('Sustained steepness, requires strength and experience.'),
        'sport_category': SportCategoryChoices.VIA_FERRATA,
    },
    SportCategoryDifficultyChoices.K6: {
        'icon': '🧗‍♂️',
        'name': _('K6 - Expert'),
        'description': _('Severe difficulty, very overhanging sections.'),
        'sport_category': SportCategoryChoices.VIA_FERRATA,
    },

    # Climbing UIAA scale
    SportCategoryDifficultyChoices.III: {
        'icon': '🧗',
        'name': _('UIAA III'),
        'description': _('Easy climbing, big holds, beginners.'),
        'sport_category': SportCategoryChoices.CLIMBING,
    },
    SportCategoryDifficultyChoices.IV: {
        'icon': '🧗',
        'name': _('UIAA IV'),
        'description': _('Moderate climbing, small holds, some exposure.'),
        'sport_category': SportCategoryChoices.CLIMBING,
    },
    SportCategoryDifficultyChoices.V: {
        'icon': '🧗',
        'name': _('UIAA V'),
        'description': _('Sustained climbing, smaller holds.'),
        'sport_category': SportCategoryChoices.CLIMBING,
    },
    SportCategoryDifficultyChoices.VI: {
        'icon': '🧗',
        'name': _('UIAA VI'),
        'description': _('Harder climbing, technical moves, advanced.'),
        'sport_category': SportCategoryChoices.CLIMBING,
    },
    SportCategoryDifficultyChoices.VII: {
        'icon': '🧗',
        'name': _('UIAA VII'),
        'description': _('Very difficult climbing, experts only.'),
        'sport_category': SportCategoryChoices.CLIMBING,
    },
}
