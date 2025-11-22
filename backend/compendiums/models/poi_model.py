# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.constants.poi_category import PoiCategoryChoices
from alpenwegs.ashared.models.creator_model import BaseCreatorModel

# AlpenWegs application import:
from compendiums.models.region_model import RegionModel

# Django import:
from django.contrib.gis.db import models


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

        # Model name values:
        verbose_name = 'Point of Interest'
        verbose_name_plural = 'Points of Interest'

        # Disable default Django permissions:
        default_permissions = ()

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_poimodel', 'Can change own pois'),
            ('change_all_poimodel', 'Can change all pois'),
            ('delete_own_poimodel', 'Can delete own pois'),
            ('delete_all_poimodel', 'Can delete all pois'),
            ('view_own_poimodel', 'Can view own pois'),
            ('view_all_poimodel', 'Can view all pois'),
            ('add_own_poimodel', 'Can add own pois'),
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

    # PoI Many-to-many relationships (reverse side):
    sections = models.ManyToManyField(
        'explorers.SectionModel',
        through='explorers.SectionToPoiModel',
        related_name='poi_sections',
        verbose_name='Sections',
        help_text='Associated Sections.',
    )
    
    # PoI transport:
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
    location = models.PointField(
        geography=True,
        srid=4326,
        verbose_name='Geographic Position (WGS84)',
        help_text='Stores the precise geolocation of the '
            'PoI using a PostGIS point.',
        blank=True,
        null=True,
    )
    elevation = models.IntegerField(
        verbose_name='Elevation (m a.s.l.)',
        help_text='Elevation of the PoI in meters above sea level.',
        blank=True,
        null=True,
    )
