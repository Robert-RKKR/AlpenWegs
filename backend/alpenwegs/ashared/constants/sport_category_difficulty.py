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

    # # Metadata class:
    # class Meta:

    #     # Additional values translation:
    #     metadata = {
    #         # Hiking T-scale
    #         121: {
    #             'icon': '🥾',
    #             'name': 'T1 - Easy Hiking',
    #             'description': 'Simple paths, well-marked, minimal risk.',
    #             'sport_category': SportCategoryChoices.HIKING,
    #         },
    #         122: {
    #             'icon': '🥾',
    #             'name': 'T2 - Mountain Hiking',
    #             'description': 'Mountain trails, more uneven ground, moderate risk.',
    #             'sport_category': SportCategoryChoices.HIKING,
    #         },
    #         123: {
    #             'icon': '🥾',
    #             'name': 'T3 - Demanding Mountain Hiking',
    #             'description': 'Exposed sections, need for surefootedness, some hands.',
    #             'sport_category': SportCategoryChoices.HIKING,
    #         },
    #         124: {
    #             'icon': '🥾',
    #             'name': 'T4 - Alpine Hiking',
    #             'description': 'Steeper terrain, occasional use of hands, high exposure.',
    #             'sport_category': SportCategoryChoices.HIKING,
    #         },
    #         125: {
    #             'icon': '🥾',
    #             'name': 'T5 - Demanding Alpine Hiking',
    #             'description': 'Very exposed, poor paths, need alpine experience.',
    #             'sport_category': SportCategoryChoices.HIKING,
    #         },
    #         126: {
    #             'icon': '🥾',
    #             'name': 'T6 - Difficult Alpine Hiking',
    #             'description': 'Exposed climbing terrain, dangerous, expert level.',
    #             'sport_category': SportCategoryChoices.HIKING,
    #         },

    #         # Via Ferrata K-scale
    #         141: {
    #             'icon': '🧗‍♂️',
    #             'name': 'K1 - Easy',
    #             'description': 'Beginner ferrata, short ladders, well-protected.',
    #             'sport_category': SportCategoryChoices.VIA_FERRATA,
    #         },
    #         142: {
    #             'icon': '🧗‍♂️',
    #             'name': 'K2 - Moderate',
    #             'description': 'Moderate climbing, some exposure.',
    #             'sport_category': SportCategoryChoices.VIA_FERRATA,
    #         },
    #         143: {
    #             'icon': '🧗‍♂️',
    #             'name': 'K3 - Difficult',
    #             'description': 'Steeper sections, higher exposure.',
    #             'sport_category': SportCategoryChoices.VIA_FERRATA,
    #         },
    #         144: {
    #             'icon': '🧗‍♂️',
    #             'name': 'K4 - Very Difficult',
    #             'description': 'Athletic climbing, vertical or overhanging.',
    #             'sport_category': SportCategoryChoices.VIA_FERRATA,
    #         },
    #         145: {
    #             'icon': '🧗‍♂️',
    #             'name': 'K5 - Extreme',
    #             'description': 'Sustained steepness, requires strength and experience.',
    #             'sport_category': SportCategoryChoices.VIA_FERRATA,
    #         },
    #         146: {
    #             'icon': '🧗‍♂️',
    #             'name': 'K6 - Expert',
    #             'description': 'Severe difficulty, very overhanging sections.',
    #             'sport_category': SportCategoryChoices.VIA_FERRATA,
    #         },

    #         # Climbing UIAA scale
    #         131: {
    #             'icon': '🧗',
    #             'name': 'UIAA III',
    #             'description': 'Easy climbing, big holds, beginners.',
    #             'sport_category': SportCategoryChoices.CLIMBING,
    #         },
    #         132: {
    #             'icon': '🧗',
    #             'name': 'UIAA IV',
    #             'description': 'Moderate climbing, small holds, some exposure.',
    #             'sport_category': SportCategoryChoices.CLIMBING,
    #         },
    #         133: {
    #             'icon': '🧗',
    #             'name': 'UIAA V',
    #             'description': 'Sustained climbing, smaller holds.',
    #             'sport_category': SportCategoryChoices.CLIMBING,
    #         },
    #         134: {
    #             'icon': '🧗',
    #             'name': 'UIAA VI',
    #             'description': 'Harder climbing, technical moves, advanced.',
    #             'sport_category': SportCategoryChoices.CLIMBING,
    #         },
    #         135: {
    #             'icon': '🧗',
    #             'name': 'UIAA VII',
    #             'description': 'Very difficult climbing, experts only.',
    #             'sport_category': SportCategoryChoices.CLIMBING,
    #         },
    #     }
