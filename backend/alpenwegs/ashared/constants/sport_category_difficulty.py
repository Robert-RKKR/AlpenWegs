# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices
from alpenwegs.ashared.constants.sport_category import SportCategoryChoices


# Choices class:
class SportCategoryDifficultyChoices(
    BaseIntegerToDictChoices,
):

    # Hiking Difficulty:
    T1 = 121, 'T1 - Easy Hiking'
    T2 = 122, 'T2 - Mountain Hiking'
    T3 = 123, 'T3 - Demanding Mountain Hiking'
    T4 = 124, 'T4 - Alpine Hiking'
    T5 = 125, 'T5 - Demanding Alpine Hiking'
    T6 = 126, 'T6 - Difficult Alpine Hiking'

    # Via Ferrata Difficulty
    K1 = 141, 'K1 - Easy'
    K2 = 142, 'K2 - Moderate'
    K3 = 143, 'K3 - Difficult'
    K4 = 144, 'K4 - Very Difficult'
    K5 = 145, 'K5 - Extreme'
    K6 = 146, 'K6 - Expert'

    # Climbing Difficulty:
    III = 131, 'UIAA III'
    IV = 132, 'UIAA IV'
    V = 133, 'UIAA V'
    VI = 134, 'UIAA VI'
    VII = 135, 'UIAA VII'

# Module-level metadata dictionary:
DIFFICULTY_METADATA =  {
    # Hiking T-scale:
    121: {
        'icon': '🟡',
        'description': 'Simple paths, well-marked, minimal risk.',
        'depend': SportCategoryChoices.HIKING,
    },
    122: {
        'icon': '🟡',
        'description': 'Mountain trails, more uneven ground, moderate risk.',
        'depend': SportCategoryChoices.HIKING,
    },
    123: {
        'icon': '🔴',
        'description': 'Exposed sections, need for surefootedness, some hands.',
        'depend': SportCategoryChoices.HIKING,
    },
    124: {
        'icon': '🔵',
        'description': 'Steeper terrain, occasional use of hands, high exposure.',
        'depend': SportCategoryChoices.HIKING,
    },
    125: {
        'icon': '⚫',
        'description': 'Very exposed, poor paths, need alpine experience.',
        'depend': SportCategoryChoices.HIKING,
    },
    126: {
        'icon': '⚫',
        'description': 'Exposed climbing terrain, dangerous, expert level.',
        'depend': SportCategoryChoices.HIKING,
    },

    # Via Ferrata K-scale:
    141: {
        'icon': '🧗‍♂️',
        'description': 'Beginner ferrata, short ladders, well-protected.',
        'depend': SportCategoryChoices.VIA_FERRATA,
    },
    142: {
        'icon': '🧗‍♂️',
        'description': 'Moderate climbing, some exposure.',
        'depend': SportCategoryChoices.VIA_FERRATA,
    },
    143: {
        'icon': '🧗‍♂️',
        'description': 'Steeper sections, higher exposure.',
        'depend': SportCategoryChoices.VIA_FERRATA,
    },
    144: {
        'icon': '🧗‍♂️',
        'description': 'Athletic climbing, vertical or overhanging.',
        'depend': SportCategoryChoices.VIA_FERRATA,
    },
    145: {
        'icon': '🧗‍♂️',
        'description': 'Sustained steepness, requires strength and experience.',
        'depend': SportCategoryChoices.VIA_FERRATA,
    },
    146: {
        'icon': '🧗‍♂️',
        'description': 'Severe difficulty, very overhanging sections.',
        'depend': SportCategoryChoices.VIA_FERRATA,
    },

    # Climbing UIAA scale:
    131: {
        'icon': '🧗',
        'description': 'Easy climbing, big holds, beginners.',
        'depend': SportCategoryChoices.CLIMBING,
    },
    132: {
        'icon': '🧗',
        'description': 'Moderate climbing, small holds, some exposure.',
        'depend': SportCategoryChoices.CLIMBING,
    },
    133: {
        'icon': '🧗',
        'description': 'Sustained climbing, smaller holds.',
        'depend': SportCategoryChoices.CLIMBING,
    },
    134: {
        'icon': '🧗',
        'description': 'Harder climbing, technical moves, advanced.',
        'depend': SportCategoryChoices.CLIMBING,
    },
    135: {
        'icon': '🧗',
        'description': 'Very difficult climbing, experts only.',
        'depend': SportCategoryChoices.CLIMBING,
    },
}
