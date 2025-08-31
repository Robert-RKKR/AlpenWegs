# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel

# AlpenWegs application import:
from compendiums.models.region_model import RegionModel

# Django import:
from django.db import models


# PoI Model class:
class PoiModel(
    BaseIdentificationModel,
    BaseTimestampModel,
    BaseCreatorModel,
):
    """
    Point of Interest (PoI) Model for storing interesting locations,
    such as bridges, mountains, peaks, rivers, shelters, etc.
    """
    

    class Meta:
        verbose_name = 'Point of Interest'
        verbose_name_plural = 'Points of Interest'

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': ['view'],
        'Author': ['view', 'add', 'change', 'delete'],
        'Admin':  ['view', 'add', 'change', 'delete'],
    }

    # PoI One-to-Many relationship:
    region = models.ForeignKey(
        RegionModel,
        verbose_name='Region ID',
        help_text='The region to which this point of interest belongs. '
        'This establishes the geographical context for the PoI.',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    # PoI Many-to-many relationships:
    # routes = models.ManyToManyField(
    #     'routes.RouteModel',
    #     through='routes.RouteToPoiModel',
    #     related_name='poi_routes',
    #     verbose_name='Routes',
    #     help_text='Associated Routes.',
    # )
    
    # PoI description:
    details_description = models.TextField(
        verbose_name='Details Description',
        help_text='Details Description of the PoI.',
        blank=True,
        null=True,
    )
    transport_description = models.BigIntegerField(
        verbose_name='Transport Description',
        help_text='Information about transport to reach this PoI.',
        blank=True,
        null=True,
    )
    
    # PoI classification:
    category = models.CharField(
        verbose_name='PoI Category',
        help_text='Xxx.',
        max_length=32,
    )
    
    # PoI Geographic Location:
    latitude = models.FloatField(
        verbose_name='Latitude',
        help_text='Geographic location of the PoI (Latitude).',
        blank=True,
        null=True,
    )
    longitude = models.FloatField(
        verbose_name='Longitude',
        help_text='Geographic location of the PoI (Longitude).',
        blank=True,
        null=True,
    )
    elevation = models.IntegerField(
        verbose_name='Elevation',
        help_text='Elevation of the PoI in meters.',
        blank=True,
        null=True,
    )
