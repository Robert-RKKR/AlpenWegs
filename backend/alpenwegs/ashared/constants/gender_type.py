# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerChoices


# Choices class:
class GenderTypeChoices(
    BaseIntegerChoices,
):

    # Choices values:
    EMPTY = 0, 'Empty'
    FEMALE = 1, 'Female'
    MALE = 2, 'Male'
