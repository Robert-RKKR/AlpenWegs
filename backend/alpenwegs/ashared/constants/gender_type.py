# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices


# Choices class:
class GenderTypeChoices(
    BaseIntegerToDictChoices,
):

    # Choices values:
    EMPTY = 0, 'Empty'
    FEMALE = 1, 'Female'
    MALE = 2, 'Male'

# Module-level metadata dictionary:
GENDER_METADATA = {
    0: {
        'icon': '⚪️',
        'description': 'No gender specified.',
        'depend': None,
    },
    1: {
        'icon': '♀️',
        'description': 'Female gender.',
        'depend': None,
    },
    2: {
        'icon': '♂️',
        'description': 'Male gender.',
        'depend': None,
    },
}
