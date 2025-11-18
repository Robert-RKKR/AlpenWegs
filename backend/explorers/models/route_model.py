# AlpenWegs import:
from alpenwegs.ashared.models.relationship_model import BaseRelationshipOrderedModel
from alpenwegs.ashared.models.characteristic_model import BaseCharacteristicModel
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
from explorers.models.section_model import SectionModel

# Django import:
from django.db import models


# Route Model class:
class RouteModel(
    BaseCharacteristicModel,
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
    Represents a single Route within the AlpenWegs system.

    A Route is a structured, ordered collection of Sections forming a
    coherent trail, itinerary, or thematic experience. It may represent
    a classic long-distance hiking trail, a multi-stage mountain bike
    itinerary, a high-alpine ridge traverse, a pilgrimage path, or any
    other meaningful outdoor route defined by AlpenWegs.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_routemodel', 'Can change own routes'),
            ('change_all_routemodel', 'Can change all routes'),
            ('delete_own_routemodel', 'Can delete own routes'),
            ('delete_all_routemodel', 'Can delete all routes'),
            ('view_own_routemodel', 'Can view own routes'),
            ('view_all_routemodel', 'Can view all routes'),
            ('add_own_routemodel', 'Can add own routes'),
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

    # Route Many-to-Many Relationships:
    sections = models.ManyToManyField(
        SectionModel,
        through='SectionToRouteModel',
        related_name='route_sections',
        verbose_name='Sections',
        help_text=(
            'The ordered list of Sections that form this Route. Sections are '
            'the atomic segments of a Route, each defining its own geometry, '
            'start/end PoIs, intermediate PoIs, regions, and characteristics. '
            'The order of Sections is controlled by the through-model '
            '"SectionToRouteModel", which includes a sequence index for '
            'precise arrangement of stage progression.'
        ),
    )


    # Route Many-to-Many Relationships (reverse side):
    trips = models.ManyToManyField(
        'TripModel',
        through='TripToRouteModel',
        related_name='route_trips',
        verbose_name='Route Trips',
        help_text=(
            'A list of Trips that incorporate this Route as part of a planned '
            'multi-day itinerary. This allows official Routes to be used as '
            'building blocks inside larger trip structures.'
        ),
    )


class SectionToRouteModel(
    BaseRelationshipOrderedModel,
    BaseDescriptiveModel,
):
    """
    An intermediate model for associating a Section
    with a route. This model allows us to store the
    relationship between a Section and a specific Route.
    """
    
    # Base relation between Many-to-many Models:
    route = models.ForeignKey(
        RouteModel,
        related_name='section_route_associations',
        verbose_name='Route',
        help_text='The Route that is associated with the Section '
            'to Route M2M relationship.',
        on_delete=models.CASCADE,
    )
    section = models.ForeignKey(
        SectionModel,
        related_name='section_trip_associations',
        verbose_name='Section',
        help_text='The Section that is associated with the Section '
            'to Trip M2M relationship.',
        on_delete=models.CASCADE,
    )
