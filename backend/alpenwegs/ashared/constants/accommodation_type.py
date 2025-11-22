# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerChoices

# Accommodation Choices class:
class AccommodationTypeChoices(
    BaseIntegerChoices,
):

    # Basic accommodation types:
    DORMITORY = 0, 'Dormitory'
    PRIVATE_ROOM = 1, 'Private Room'
    HOTEL = 2, 'Hotel'

    # Outdoor accommodation types:
    TENT = 10, 'Tent'
    CAMPING = 11, 'Camping Site'
    BIVOUAC = 12, 'Bivouac Spot'

    # Mountain-specific accommodation types:
    MOUNTAIN_HUT = 20, 'Mountain Hut'
    ALPINE_HUT = 21, 'Alpine Hut'
    WINTER_HUT = 22, 'Winter Hut'

    # Specialty / long-distance accommodation:
    HOSTEL = 30, 'Hostel'
    GUESTHOUSE = 31, 'Guesthouse'
    CABIN = 32, 'Cabin / Lodge'

    # Mixed or flexible:
    MIXED = 40, 'Mixed Accommodation'
