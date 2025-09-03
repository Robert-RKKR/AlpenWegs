# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.constants.poi_category import PoiCategoryChoices
from alpenwegs.ashared.models.creator_model import BaseCreatorModel

# AlpenWegs application import:
from compendiums.models.region_model import RegionModel

# Django import:
from django.db import models


# PoI Model class:
class PoiModel(
    BaseIdentificationModel,
    BaseDescriptiveModel,
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
    transport_description = models.BigIntegerField(
        verbose_name='Transport Description',
        help_text='Information about how to reach this PoI '
            '(roads, trails, public transport).',
        blank=True,
        null=True,
    )
    
    # PoI classification:
    category = models.IntegerField(
        choices=PoiCategoryChoices.choices,
        verbose_name='Category',
        help_text='Classification of this Point of Interest '
            '(e.g. City, Village, Hut, Peak, Lake, Pass).',
        default=PoiCategoryChoices.OTHER,
    )
    
    # PoI Geographic Location:
    latitude = models.FloatField(
        verbose_name='Latitude',
        help_text='Latitude in decimal degrees (WGS84). '
            'Used for map display and spatial queries.',
        blank=True,
        null=True,
    )
    longitude = models.FloatField(
        verbose_name='Longitude',
        help_text='Longitude in decimal degrees (WGS84). '
            'Used for map display and spatial queries.',
        blank=True,
        null=True,
    )
    elevation = models.IntegerField(
        verbose_name='Elevation (m a.s.l.)',
        help_text='Elevation of the PoI in meters above sea level.',
        blank=True,
        null=True,
    )
