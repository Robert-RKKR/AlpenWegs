# Application import:
from wanderswiss.base.models.identification_model import BaseIdentificationModel
from wanderswiss.base.models.relationship_model import BaseRelationshipModel
from wanderswiss.base.models.timestamp_model import BaseTimestampModel
from wanderswiss.base.models.statistic_model import BaseStatisticModel
from wanderswiss.base.models.creator_model import BaseCreatorModel
from wanderswiss.base.models.score_model import BaseScoreModel
from routes.models.base.base_gpx_model import BaseGpxModel
from compendium.models.region_model import RegionModel
from compendium.models.card_model import CardModel
from assets.models.photo_model import PhotoModel
from compendium.models.poi_model import PoiModel

# Django import:
from django.db import models


# Route Model class:
class RouteModel(
    BaseIdentificationModel,
    BaseTimestampModel,
    BaseStatisticModel,
    BaseCreatorModel,
    BaseScoreModel,
    BaseGpxModel):
    """
    Model representing routes.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    # Route Many-to-Many Relationships:
    photos = models.ManyToManyField(
        PhotoModel,
        through='RouteToPhotoModel',
        related_name='route_photos',
        verbose_name='Route Photos',
        help_text='A collection of photos that are linked to '
            'the route and that provide a visual documentation '
            'of the route created by the route creator.'
    )
    pois = models.ManyToManyField(
        PoiModel,
        through='RouteToPoiModel',
        related_name='route_pois',
        verbose_name='Route Points of Interest (PoIs)',
        help_text='A list of Points of Interest associated '
            'with the route, highlighting key places for travelers '
            'to visit along the way. Points of Interest also '
            'mark the start and end points of the route.'
    )
    cards = models.ManyToManyField(
        CardModel,
        through='RouteToCardModel',
        related_name='route_cards',
        verbose_name='Route Cards',
        help_text='Cards associated with the route that can '
            'be obtained by the user by completing this route.'
    )
    regions = models.ManyToManyField(
        RegionModel,
        through='RouteToRegionModel',
        related_name='route_regions',
        verbose_name='Route Regions',
        help_text='Geographical regions through which the '
            'route passes.'
    )
    multiday_routes = models.ManyToManyField(
        'MultidayRouteModel',
        through='MultidayRouteToRouteModel',
        related_name='route_multiday_routes',
        verbose_name='Route Multiday Routes',
        help_text='Multi-day routes that include this route '
            'as part of a multi-day experience.'
    )
    
    # Route Many-to-Many Relationships with User Model:
    users_accomplished = models.ManyToManyField(
        'profiles.UserModel',
        through='profiles.UserToRouteAccomplishedModel',
        related_name='route_users_accomplished',
        verbose_name='Users Accomplished',
        help_text='Users that accomplished this route.'
    )
    users_liked = models.ManyToManyField(
        'profiles.UserModel',
        through='profiles.UserToRouteLikedModel',
        related_name='route_users_liked',
        verbose_name='Users Liked',
        help_text='Users that liked this route.'
    )

    # Route classification:
    category = models.CharField(
        verbose_name='Route Category',
        help_text='Route category.',
        max_length=32,
    )

    # Descriptive Fields:
    description = models.TextField(
        verbose_name='Route Description',
        help_text='A detailed description of the route, including '
            'user-specified information such as terrain, difficulty '
            'level, notable landmarks, scenic highlights, and '
            'any additional insights provided by the creator.',
        blank=True,
        null=True,
    )

    # Route level characteristics:
    difficulty = models.CharField(
        verbose_name='General Difficulty Level',
        help_text='Overall difficulty level of the route. Options '
            'include: Easy, Moderate, Difficult, Very Difficult, '
            'and Extremely Difficult routes.',
        max_length=32,
        blank=True,
        null=True,
    )
    type_specific_difficulty = models.CharField(
        verbose_name='Route Type-Specific Difficulty',
        help_text='Difficulty level specific to the route category. '
            'For example, hiking routes use T1-T6, via ferrata '
            'routes use K1-K6, and other categories have their '
            'own grading systems.',
        max_length=32,
        blank=True,
        null=True,
    )
    stamina_requirement = models.CharField(
        verbose_name='Stamina Requirement',
        help_text='Level of stamina required to complete the route.',
        max_length=32,
        blank=True,
        null=True,
    )
    experience_requirement = models.CharField(
        verbose_name='Experience Requirement',
        help_text='Level of experience required to safely '
            'complete the entire route.',
        max_length=32,
        blank=True,
        null=True,
    )
    potential_risk_requirement = models.CharField(
        verbose_name='Risk Requirement',
        help_text='Potential risks associated with this route.',
        max_length=32,
        blank=True,
        null=True,
    )
    potential_risk_description = models.CharField(
        verbose_name='Risk Description',
        help_text='Detailed description of possible hazards along the route.',
        max_length=8192,
        blank=True,
        null=True,
    )

    # Seasonal Information:
    best_seasons = models.CharField(
        verbose_name='Best Seasons',
        help_text='Best seasons for hiking this route.',
        max_length=32,
        blank=True,
        null=True,
    )
    best_months = models.JSONField(
        verbose_name='Best Months',
        help_text='List of best months to complete this route.',
        blank=True,
        null=True,
    )
    winter_season = models.BooleanField(
        verbose_name='Available in Winter',
        help_text='Indicates if the route is accessible in winter.',
        blank=True,
        null=True,
    )
    summer_season = models.BooleanField(
        verbose_name='Available in Summer',
        help_text='Indicates if the route is accessible in summer.',
        blank=True,
        null=True,
    )
    family_friendly = models.BooleanField(
        verbose_name='Family Friendly',
        help_text='Indicates if the route is suitable for families.',
        blank=True,
        null=True,
    )

    # Statistic Information:
    accomplished_count = models.BigIntegerField(
        verbose_name='Accomplished Count',
        help_text='Total number of users who have ''completed this route.',
        default=0,
    )
    like_count = models.BigIntegerField(
        verbose_name='Like Count',
        help_text='Total number of likes received by this route.',
        default=0,
    )

    # API-Related Fields
    photo_primary = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    user_difficulty = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    user_duration = models.BigIntegerField(
        blank=True,
        null=True,
    )


# Router Model Many-to-many relationships with other models:
class RouteToPoiModel(BaseRelationshipModel):
    """
    An intermediate model for associating a Point of Interest
    (PoI) with a route. This model allows us to store the
    relationship between a PoI and a specific route.
    """
    
    # Base relation between Many-to-many Models:
    route = models.ForeignKey(
        RouteModel,
        related_name='poi_route_associations',
        verbose_name='Route',
        help_text='The route that this point of interest is associated with.',
        on_delete=models.CASCADE,
    )
    poi = models.ForeignKey(
        PoiModel,
        related_name='route_poi_associations',
        verbose_name='Point of Interest',
        help_text='The point of interest associated with a route.',
        on_delete=models.CASCADE,
    )
    
    # PoI role in relation to route:
    start_point = models.BooleanField(
        default=False,
        verbose_name='Is Start Point',
        help_text='Indicates whether this point of interest is the '
            'starting point of the associated route. If True, this PoI '
            'marks the beginning of the route; otherwise, it is other '
            'typ of associated PoI like end or middle point.',
    )
    end_point = models.BooleanField(
        default=False,
        verbose_name='Is End Point',
        help_text='Indicates whether this point of interest is the '
            'ending point of the associated route. If True, this PoI '
            'marks the end of the route; otherwise, it is other '
            'typ of associated PoI like beginning or middle point.',
    )
    middle_point = models.BooleanField(
        default=False,
        verbose_name='Is Middle Point',
        help_text='Indicates whether this point of interest is the '
            'middle point of the associated route. If True, this PoI '
            'is considered as a middle or intermediate point along '
            'the route; otherwise, it is other typ of associated '
            'PoI like beginning or end point of the route.',
    )


class RouteToPhotoModel(BaseRelationshipModel):
    """
    An intermediate model for associating a Photo
    with a route. This model allows us to store the
    relationship between a Photo and a specific route.
    """
    
    # Base relation between Many-to-many Models:
    route = models.ForeignKey(
        RouteModel,
        related_name='photo_route_associations',
        verbose_name='Route',
        help_text='The route that this point of interest is associated with.',
        on_delete=models.CASCADE,
    )
    photo = models.ForeignKey(
        PhotoModel,
        related_name='route_photo_associations',
        verbose_name='Photo',
        help_text='Xxx.',
        on_delete=models.CASCADE,
    )


class RouteToCardModel(BaseRelationshipModel):
    """
    An intermediate model for associating a card
    with a route. This model allows us to store the
    relationship between a Card and a specific route.
    """
    
    # Base relation between Many-to-many Models:
    route = models.ForeignKey(
        RouteModel,
        related_name='card_route_associations',
        verbose_name='Route',
        help_text='The route that this point of interest is associated with.',
        on_delete=models.CASCADE,
    )
    card = models.ForeignKey(
        CardModel,
        related_name='route_card_associations',
        verbose_name='Card',
        help_text='Xxx.',
        on_delete=models.CASCADE,
    )


class RouteToRegionModel(BaseRelationshipModel):
    """
    An intermediate model for associating a region
    with a route. This model allows us to store the
    relationship between a Card and a specific route.
    """
    
    # Base relation between Many-to-many Models:
    route = models.ForeignKey(
        RouteModel,
        related_name='region_route_associations',
        verbose_name='Route',
        help_text='The route that this point of interest is associated with.',
        on_delete=models.CASCADE,
    )
    region = models.ForeignKey(
        RegionModel,
        related_name='route_region_associations',
        verbose_name='Region',
        help_text='Xxx.',
        on_delete=models.CASCADE,
    )
