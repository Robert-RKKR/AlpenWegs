# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.constants.country import CountryChoices

# Django import:
from django.db import models


# Region Model class:
class RegionModel(
    BaseIdentificationModel,
    BaseTimestampModel,
    BaseCreatorModel,
):
    """
    Region Model for storing details about a specific region within a country.
    """

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': ['view'],
        'Author': ['view', 'add', 'change', 'delete'],
        'Admin':  ['view', 'add', 'change', 'delete'],
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
    description = models.TextField(
        verbose_name='Region Description',
        help_text='A description of the region.',
    )
    
    # Region Geographic Location:
    latitude = models.FloatField(
        verbose_name='Latitude',
        help_text='Geographic location of the Region (Latitude).',
        blank=True,
        null=True,
    )
    longitude = models.FloatField(
        verbose_name='Longitude',
        help_text='Geographic location of the Region (Longitude).',
        blank=True,
        null=True,
    )
