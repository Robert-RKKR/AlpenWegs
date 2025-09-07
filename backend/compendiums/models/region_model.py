# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.constants.country import CountryChoices

# Django import:
from django.db import models


# Region Model class:
class RegionModel(
    BaseIdentificationModel,
    BaseDescriptiveModel,
    BaseTimestampModel,
    BaseCreatorModel,
):
    """
    Region Model for storing details about a specific region within a country.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

        # Disable default Django permissions:
        default_permissions = ()

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_regionmodel', 'Can change own regions'),
            ('change_all_regionmodel', 'Can change all regions'),
            ('delete_own_regionmodel', 'Can delete own regions'),
            ('delete_all_regionmodel', 'Can delete all regions'),
            ('view_own_regionmodel', 'Can view own regions'),
            ('view_all_regionmodel', 'Can view all regions'),
            ('add_own_regionmodel', 'Can add own regions'),
        ]

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': [
            'view_all',
            'view_own',
        ],
        'Author': [
            'change_own',
            'delete_own',
            'view_all',
            'view_own',
            'add_own',
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
    
    # Region Many-to-many relationship:
    # routes = models.ManyToManyField(
    #     'routes.RouteModel',
    #     through='routes.RouteToRegionModel',
    #     related_name='region_routes',
    #     verbose_name='Routes',
    #     help_text='Associated Routes.',
    # )

    # Region specific values:
    country = models.IntegerField(
        choices=CountryChoices.choices,
        verbose_name='Country',
        help_text='Country where the region is located (fixed numeric list).',
        default=CountryChoices.SWITZERLAND,
    )
