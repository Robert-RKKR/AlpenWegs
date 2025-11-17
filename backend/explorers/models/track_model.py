# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.sport_category_model import BaseSportCategoryModel
from alpenwegs.ashared.models.accomplished_model import BaseAccomplishedModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.statistic_model import BaseStatisticModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.gpx_track_model import BaseGpxTrackModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.models.liked_model import BaseLikedModel
from alpenwegs.ashared.models.score_model import BaseScoreModel

# AlpenWegs application import:
from explorers.models.journey_model import JourneyModel

# Django import:
from django.db import models


# Track Model class:
class TrackModel(
    BaseIdentificationModel,
    BaseSportCategoryModel,
    BaseAccomplishedModel,
    BaseDescriptiveModel,
    BaseTimestampModel,
    BaseStatisticModel,
    BaseCreatorModel,
    BaseLikedModel,
    BaseScoreModel,
    BaseGpxTrackModel,
):
    """
    Model representing a single recorded Track (user activity).
    """

    class Meta:

        # Model name values:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_trackmodel', 'Can change own tracks'),
            ('change_all_trackmodel', 'Can change all tracks'),
            ('delete_own_trackmodel', 'Can delete own tracks'),
            ('delete_all_trackmodel', 'Can delete all tracks'),
            ('view_own_trackmodel', 'Can view own tracks'),
            ('view_all_trackmodel', 'Can view all tracks'),
            ('add_own_trackmodel', 'Can add own tracks'),
        ]

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own',
        ],
        'Author': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own',
        ],
        'Admin': [
            'change_all',
            'change_own',
            'delete_all',
            'delete_own',
            'view_all',
            'view_own',
            'add_own',
        ],
    }

    # Track Many-to-Many Relationships (reverse side):
    journey = models.ForeignKey(
        JourneyModel,
        verbose_name='Related Journey',
        help_text='Optional Journey that this Track is part of.',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # Track metadata:
    verified = models.BooleanField(
        verbose_name='Verified Track',
        help_text='Indicates whether this Track has been verified '
            'against an official Route or Section.',
        default=False,
    )
    similarity_index = models.FloatField(
        verbose_name='Similarity Index (%)',
        help_text='Degree of match between this Track and the official '
            'Route or Section, measured as a percentage (0–100%).',
        blank=True,
        null=True,
    )
    user_notes = models.TextField(
        verbose_name='User Notes',
        help_text='Personal notes or observations recorded by the user '
            'for this activity (weather, conditions, remarks, etc.).',
        blank=True,
        null=True,
    )
