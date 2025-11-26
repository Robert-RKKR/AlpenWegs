# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices


# Choices class:
class ActionTypeChoices(
    BaseIntegerToDictChoices,
):

    # Choices values:
    EMPTY = 0, 'Empty'
    CREATE = 1, 'Create'
    UPDATE = 2, 'Update'
    DELETE = 3, 'Delete'

# Module-level metadata dictionary:
ACTION_TYPE_METADATA = {
    0: {
        'icon': '⚪️',
        'description': 'No action has been recorded.',
        'depend': None,
    },
    1: {
        'icon': '➕',
        'description': 'Object has been created.',
        'depend': None,
    },
    2: {
        'icon': '✏️',
        'description': 'Object has been updated.',
        'depend': None,
    },
    3: {
        'icon': '🗑️',
        'description': 'Object has been deleted.',
        'depend': None,
    },
}
