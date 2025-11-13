# AlpenWegs import:
from alpenwegs.ashared.models.relationship_model import BaseRelationshipOrderedModel
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.sport_category_model import BaseSportCategoryModel
from alpenwegs.ashared.models.accomplished_model import BaseAccomplishedModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.statistic_model import BaseStatisticModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.models.liked_model import BaseLikedModel
from alpenwegs.ashared.models.score_model import BaseScoreModel

# AlpenWegs application import:
from compendiums.models.poi_model import PoiModel
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
    BaseCreatorModel,
    BaseLikedModel,
    BaseScoreModel,
):
    """
    Model representing a user-recorded multi-day Journey experience.
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

    # Journey Many-to-Many Relationships:
    tracks = models.ManyToManyField(
        'TrackModel',
        through='JourneyToTrackModel',
        related_name='journey_tracks',
        verbose_name='Tracks',
        help_text='Recorded Tracks associated with this multi-day Journey.',
    )

    # Journey related Information:
    trip = models.ForeignKey(
        TripModel,
        verbose_name='Related Trip',
        help_text='Optional reference to a predefined Trip '
            'that this Journey corresponds to.',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    start_date = models.DateField(
        verbose_name='Start Date',
        help_text='Date when the Journey began.',
        blank=True,
        null=True,
    )
    end_date = models.DateField(
        verbose_name='End Date',
        help_text='Date when the Journey finished.',
        blank=True,
        null=True,
    )
    total_days = models.IntegerField(
        verbose_name='Total Days',
        help_text='Total number of days in this Journey. Automatically calculated from associated Tracks if not provided.',
        blank=True,
        null=True,
    )


# JourneyToTrack relationship model:
class JourneyToTrackModel(
    BaseRelationshipOrderedModel,
    BaseDescriptiveModel,
):
    """
    Intermediate model for associating Journeys with Tracks.
    """

    # Base relation between Many-to-many Models:
    journey = models.ForeignKey(
        JourneyModel,
        related_name='track_journey_associations',
        verbose_name='Journey',
        help_text='The Journey that is associated with the Track '
            'to Journey M2M relationship.',
        on_delete=models.CASCADE,
    )
    track = models.ForeignKey(
        TrackModel,
        related_name='journey_track_associations',
        verbose_name='Track',
        help_text='The Track that is associated with the Journey '
            'to Track M2M relationship.',
        on_delete=models.CASCADE,
    )
    
    # Relation with other models:
    poi = models.ForeignKey(
        PoiModel,
        verbose_name='Point of Interest',
        help_text='The point of interest associated with '
            'Journey to Track M2M relationship.',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
