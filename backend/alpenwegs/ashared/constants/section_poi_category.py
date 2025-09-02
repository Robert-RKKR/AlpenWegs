# AlpenWeg import:
from alpenwegs.ashared.constants.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class SectionPoiRoleChoices(
    BaseIntegerChoices,
):

    # Choices values:
    START = 1, 'Start'
    VIA   = 2,   'Via'
    END   = 3,   'End'
