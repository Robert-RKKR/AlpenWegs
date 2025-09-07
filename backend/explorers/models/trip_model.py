# AlpenWegs import:
from alpenwegs.ashared.models.relationship_model import BaseRelationshipOrderedModel
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.sport_category_model import BaseSportCategoryModel
from alpenwegs.ashared.models.accomplished_model import BaseAccomplishedModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.statistic_model import BaseStatisticModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.models.liked_model import BaseLikedModel
from alpenwegs.ashared.models.score_model import BaseScoreModel

# AlpenWegs application import:
from explorers.models.route_model import RouteModel
from compendiums.models.poi_model import PoiModel

# Django import:
from django.db import models


# Trip Model class:
class TripModel(
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
    Model representing single multi-day Trip.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_tripmodel', 'Can change own trips'),
            ('change_all_tripmodel', 'Can change all trips'),
            ('delete_own_tripmodel', 'Can delete own trips'),
            ('delete_all_tripmodel', 'Can delete all trips'),
            ('view_own_tripmodel', 'Can view own trips'),
            ('view_all_tripmodel', 'Can view all trips'),
            ('add_own_tripmodel', 'Can add own trips'),
        ]

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': ['change_own', 'delete_own', 'view_own', 'add_own'],
        'Author': ['change_own', 'delete_own', 'view_own', 'add_own'],
        'Admin':  ['change_all', 'delete_all', 'view_all', 'add_own'],
    }

    # Trip Many-to-Many Relationships:
    routes = models.ManyToManyField(
        RouteModel,
        through='TripToRouteModel',
        related_name='trip_routes',
        verbose_name='Routes',
        help_text='Associated Routes.',
    )
    
    # Trip related Information:
    days = models.IntegerField(
        verbose_name='Days',
        help_text='Amount of days the multi-day route takes.' 
    )


class TripToRouteModel(
    BaseRelationshipOrderedModel,
    BaseDescriptiveModel,
):
    """
    An intermediate model for associating a Trip
    with a route. This model allows us to store the
    relationship between a Trip and a specific Route.
    """
    
    # Base relation between Many-to-many Models:
    trip = models.ForeignKey(
        TripModel,
        related_name='route_trip_associations',
        verbose_name='Trip',
        help_text='The Trip that is associated with the Route '
            'to Trip M2M relationship.',
        on_delete=models.CASCADE,
    )
    route = models.ForeignKey(
        RouteModel,
        related_name='trip_route_associations',
        verbose_name='Route',
        help_text='The Route that is associated with the Trip '
            'to Route M2M relationship.',
        on_delete=models.CASCADE,
    )
    
    # Relation with other models:
    poi = models.ForeignKey(
        PoiModel,
        verbose_name='Point of Interest',
        help_text='The point of interest associated with '
            'Route to Trip M2M relationship.',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
