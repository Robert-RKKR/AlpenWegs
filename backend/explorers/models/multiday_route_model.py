# Application import:
from wanderswiss.base.models.identification_model import BaseIdentificationModel
from wanderswiss.base.models.relationship_model import BaseRelationshipModel
from wanderswiss.base.models.timestamp_model import BaseTimestampModel
from wanderswiss.base.models.statistic_model import BaseStatisticModel
from wanderswiss.base.models.creator_model import BaseCreatorModel
from compendium.models.poi_model import PoiModel
from .route_model import RouteModel

# Django import:
from django.db import models


# Multiday Route Model class:
class MultidayRouteModel(
    BaseIdentificationModel,
    BaseTimestampModel,
    BaseStatisticModel,
    BaseCreatorModel):
    """
    Model representing routes.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Multiday Route'
        verbose_name_plural = 'Multiday Routes'

    # Multiday Route Many-to-Many Relationships:
    routes = models.ManyToManyField(
        RouteModel,
        through='MultidayRouteToRouteModel',
        related_name='multiday_route_routes',
        verbose_name='Routes',
        help_text='Associated Routes.',
    )
    
    # Multiday Route Many-to-Many Relationships with User Model:
    users_accomplished = models.ManyToManyField(
        'profiles.UserModel',
        through='profiles.UserToMultidayRouteAccomplishedModel',
        related_name='multiday_route_users_accomplished',
        verbose_name='Users Accomplished',
        help_text='Users that accomplished this muli-day route.'
    )
    users_liked = models.ManyToManyField(
        'profiles.UserModel',
        through='profiles.UserToMultidayRouteLikedModel',
        related_name='multiday_route_users_liked',
        verbose_name='Users Liked',
        help_text='Users that liked this muli-day route.'
    )
    
    # Multiday Route description:
    details_description = models.TextField(
        verbose_name='Details Description',
        help_text='Details Description of the PoI.',
        blank=True,
        null=True,
    )
    
    # Multiday Route related Information:
    days = models.IntegerField(
        verbose_name='Days',
        help_text='Amount of days the multi-day route takes.' 
    )

    # Statistic Information:
    accomplished_count = models.BigIntegerField(
        verbose_name='Accomplished Count',
        help_text='Total number of users who have '
        'completed this multi-day route.',
        blank=False,
        null=False,
        default=0,
    )
    like_count = models.BigIntegerField(
        verbose_name='Like Count',
        help_text='Total number of likes received '
        'by this multi-day route.',
        blank=False,
        null=False,
        default=0,
    )


class MultidayRouteToRouteModel(BaseRelationshipModel):
    """
    An intermediate model for associating a multiday route
    with a route. This model allows us to store the
    relationship between a Card and a specific route.
    """
    
    # Base relation between Many-to-many Models:
    multiday_route = models.ForeignKey(
        MultidayRouteModel,
        related_name='route_multiday_route_associations',
        verbose_name='Multiday Route',
        help_text='The multiday route that this route is associated with.',
        on_delete=models.CASCADE,
    )
    route = models.ForeignKey(
        RouteModel,
        related_name='multiday_route_route_associations',
        verbose_name='Route',
        help_text='The route that this multiday route is associated with.',
        on_delete=models.CASCADE,
    )
    
    # Relation with other models:
    poi = models.ForeignKey(
        PoiModel,
        verbose_name='Point of Interest',
        help_text='The point of interest associated with a route.',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    # Accommodation description:
    description = models.TextField(
        verbose_name='Accommodation Description',
        help_text='Details accomodation description.',
        blank=True,
        null=True,
    )
