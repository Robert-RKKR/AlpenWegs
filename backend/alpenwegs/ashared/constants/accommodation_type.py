# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Accommodation Choices class:
class AccommodationTypeChoices(
    BaseIntegerChoices,
):

    # Basic accommodation types:
    DORMITORY = 0, _('Dormitory')
    PRIVATE_ROOM = 1, _('Private Room')
    HOTEL = 2, _('Hotel')

    # Outdoor accommodation types:
    TENT = 10, _('Tent')
    CAMPING = 11, _('Camping Site')
    BIVOUAC = 12, _('Bivouac Spot')

    # Mountain-specific accommodation types:
    MOUNTAIN_HUT = 20, _('Mountain Hut')
    ALPINE_HUT = 21, _('Alpine Hut')
    WINTER_HUT = 22, _('Winter Hut')

    # Specialty / long-distance accommodation:
    HOSTEL = 30, _('Hostel')
    GUESTHOUSE = 31, _('Guesthouse')
    CABIN = 32, _('Cabin / Lodge')

    # Mixed or flexible:
    MIXED = 40, _('Mixed Accommodation')
