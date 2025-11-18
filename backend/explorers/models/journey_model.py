# AlpenWegs import:
from alpenwegs.ashared.constants.accommodation_type import AccommodationTypeChoices
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.sport_category_model import BaseSportCategoryModel
from alpenwegs.ashared.models.accomplished_model import BaseAccomplishedModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.statistic_model import BaseStatisticModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.multi_day_model import BaseMultiDayModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.models.liked_model import BaseLikedModel
from alpenwegs.ashared.models.score_model import BaseScoreModel

# AlpenWegs application import:
from explorers.models.trip_model import TripModel

# Django import:
from django.db import models


# Journey Model class:
class JourneyModel(
    BaseIdentificationModel,
    BaseSportCategoryModel,
    BaseAccomplishedModel,
    BaseDescriptiveModel,
    BaseTimestampModel,
    BaseStatisticModel,
    BaseMultiDayModel,
    BaseCreatorModel,
    BaseLikedModel,
    BaseScoreModel,
):
    """
    Represents a user-created multi-day Journey. A Journey groups several
    Tracks into a single structured outdoor experience, providing the
    chronological and narrative framework for extended hiking tours,
    long-distance bike efforts, multi-stage trail runs, or similar
    multi-day outdoor objectives. A Journey may optionally reference a
    predefined Trip template, indicating that the user intended to follow
    or approximate an official multi-day itinerary. Individual Tracks within
    the Journey may also link to official Routes, allowing comparison
    between the user’s recorded segments and known trails. Together, the
    Journey, its Tracks, and any associated Trips or Routes form a complete
    representation of a multi-day adventure.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Journey'
        verbose_name_plural = 'Journeys'

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_journeymodel', 'Can change own journeys'),
            ('change_all_journeymodel', 'Can change all journeys'),
            ('delete_own_journeymodel', 'Can delete own journeys'),
            ('delete_all_journeymodel', 'Can delete all journeys'),
            ('view_own_journeymodel', 'Can view own journeys'),
            ('view_all_journeymodel', 'Can view all journeys'),
            ('add_own_journeymodel', 'Can add own journeys'),
        ]

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own'
        ],
        'Author': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own'
        ],
        'Admin':  [
            'change_all',
            'change_own',
            'delete_all',
            'delete_own',
            'view_all',
            'view_own',
            'add_own',
        ],
    }

    # Journey Many-to-One Relationship:
    trip = models.ForeignKey(
        TripModel,
        verbose_name='Related Trip',
        help_text=(
            'Optional reference to a predefined Trip template. Trips define '
            'recommended multi-day structures or official AlpenWegs routes. '
            'Linking a Journey to a Trip allows comparing actual progress '
            'with a predefined plan or map-based itinerary.'
        ),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
