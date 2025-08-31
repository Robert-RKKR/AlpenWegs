# Application import:
from wanderswiss.base.models.relationship_model import BaseRelationshipModel
from routes.models.base.base_user_gpx_model import BaseGpxUserModel
from routes.models.multiday_route_model import MultidayRouteModel
from compendium.models.card_model import CardModel
from routes.models.route_model import RouteModel
from profiles.models.user_model import UserModel

# Django import:
from django.db import models


# User to Route Many-to-Many Relationships Models:
class UserToRouteAccomplishedModel(
    BaseRelationshipModel,
    BaseGpxUserModel):
    """
    Represents a many-to-many relationship between users and routes
    they have accomplished. This model tracks which users have
    successfully completed specific routes.
    """

    class Meta:

        # Model name values:
        verbose_name = 'User to Route Accomplished'
        verbose_name_plural = 'Users to Routes Accomplished'
    
    # Base relation between Many-to-many Models:
    user = models.ForeignKey(
        UserModel,
        related_name='route_user_accomplished_associations',
        verbose_name='User',
        help_text='The user who has accomplished this route.',
        on_delete=models.CASCADE,
    )
    route = models.ForeignKey(
        RouteModel,
        related_name='user_route_accomplished_associations',
        verbose_name='Route',
        help_text='The route that has been accomplished by the user.',
        on_delete=models.CASCADE,
    )

    # Route accomplish related information:
    accomplished_winter = models.BooleanField(
        verbose_name='Route Accomplished in Winter',
        help_text='Indicates if the route was accomplished during winter.',
        default=False,
    )
    accomplished_group = models.BooleanField(
        verbose_name='Route Accomplished with Group',
        help_text='Indicates if the route was accomplished with '
            'other people (group) or alone (solo).',
        default=False,
    )


class UserToRouteLikedModel(BaseRelationshipModel):
    """
    Represents a many-to-many relationship between users and routes
    they have liked. This model tracks user interactions where a
    route is marked as liked, with optional comments.
    """

    class Meta:

        # Model name values:
        verbose_name = 'User to Route Liked'
        verbose_name_plural = 'Users to Routes Liked'
    
    # Base relation between Many-to-many Models:
    user = models.ForeignKey(
        UserModel,
        related_name='route_user_liked_associations',
        verbose_name='User',
        help_text='The user who liked this route.',
        on_delete=models.CASCADE,
    )
    route = models.ForeignKey(
        RouteModel,
        related_name='user_route_liked_associations',
        verbose_name='Route',
        help_text='The route that has been liked by the user.',
        on_delete=models.CASCADE,
    )
    
    # User comments fields:
    comment = models.CharField(
        verbose_name='Comment',
        help_text='Optional comment about why the user liked the route.',
        max_length=256,
        blank=True,
        null=True,
    )


# User to Multiday Route Many-to-Many Relationships Models:
class UserToMultidayRouteAccomplishedModel(
    BaseRelationshipModel,
    BaseGpxUserModel):
    """
    Represents a many-to-many relationship between users and multiday
    routes they have accomplished. This model tracks which users
    have successfully completed specific multiday routes.
    """

    class Meta:

        # Model name values:
        verbose_name = 'User to Multiday Route Accomplished'
        verbose_name_plural = 'Users to Multiday Routes Accomplished'
    
    # Base relation between Many-to-many Models:
    user = models.ForeignKey(
        UserModel,
        related_name='multiday_route_user_accomplished_associations',
        verbose_name='User',
        help_text='The user who has accomplished this multiday route.',
        on_delete=models.CASCADE,
    )
    multiday_route = models.ForeignKey(
        MultidayRouteModel,
        related_name='user_multiday_route_accomplished_associations',
        verbose_name='Multiday Route',
        help_text='The multiday route that has been accomplished by the user.',
        on_delete=models.CASCADE,
    )

    # Multiday Route accomplish related information:
    accomplished_winter = models.BooleanField(
        verbose_name='Route Accomplished in Winter',
        help_text='Indicates if the route was accomplished during winter.',
        default=False,
    )
    accomplished_group = models.BooleanField(
        verbose_name='Route Accomplished with Group',
        help_text='Indicates if the route was accomplished with '
            'other people (group) or alone (solo).',
        default=False,
    )


class UserToMultidayRouteLikedModel(BaseRelationshipModel):
    """
    Represents a many-to-many relationship between users and multiday routes
    they have liked. This model tracks user interactions where a multiday
    route is marked as liked, with optional comments.
    """

    class Meta:

        # Model name values:
        verbose_name = 'User to Multiday Route Liked'
        verbose_name_plural = 'Users to Multiday Routes Liked'
    
    # Base relation between Many-to-many Models:
    user = models.ForeignKey(
        UserModel,
        related_name='multiday_route_user_liked_associations',
        verbose_name='User',
        help_text='The user who liked this multiday route.',
        on_delete=models.CASCADE,
    )
    multiday_route = models.ForeignKey(
        MultidayRouteModel,
        related_name='user_multiday_route_liked_associations',
        verbose_name='Multiday Route',
        help_text='The multiday route that has been liked by the user.',
        on_delete=models.CASCADE,
    )
    
    # User comments fields:
    comment = models.CharField(
        verbose_name='Comment',
        help_text='Optional comment about why the user '
            'liked the multiday route.',
        max_length=256,
        blank=True,
        null=True,
    )


# Other User Many-to-Many Relationships Models:
class UserToCardModel(BaseRelationshipModel):
    """
    Represents a many-to-many relationship between users and cards
    they have earned or collected. This model tracks which users
    have received or are associated with specific card.
    """

    class Meta:

        # Model name values:
        verbose_name = 'User to Card'
        verbose_name_plural = 'Users to Cards'
    
    # Base relation between Many-to-many Models:
    user = models.ForeignKey(
        UserModel,
        related_name='card_user_associations',
        verbose_name='User',
        help_text='The user who owns or is associated with this card.',
        on_delete=models.CASCADE,
    )
    card = models.ForeignKey(
        CardModel,
        related_name='user_card_associations',
        verbose_name='Card',
        help_text='The card that the user owns or is associated with.',
        on_delete=models.CASCADE,
    )
