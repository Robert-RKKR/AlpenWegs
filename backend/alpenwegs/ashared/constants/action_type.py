# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerChoices


# Choices class:
class ActionTypeChoices(
    BaseIntegerChoices,
):

    # Choices values:
    EMPTY = 0, 'Empty'
    CREATE = 1, 'Create'
    UPDATE = 2, 'Update'
    DELETE = 3, 'Delete'
