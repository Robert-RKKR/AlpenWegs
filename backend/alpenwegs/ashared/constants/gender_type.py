# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class GenderTypeChoices(
    BaseIntegerChoices,
):

    # Choices values:
    EMPTY = 0, _('Empty')
    FEMALE = 1, _('Female')
    MALE = 2, _('Male')
