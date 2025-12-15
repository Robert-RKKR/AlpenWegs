"""
Abstract GPX Localization Model
-------------------------------

This abstract model represents localized geographic information
derived from GPX data. It is designed to store spatial reference
points and elevation context extracted from a GPX track, enabling
precise geolocation, spatial indexing, and map-based interactions.

Rather than representing a full route, this model focuses on
key localization attributes such as coordinates and elevation,
which can be reused by higher-level models (routes, segments,
points of interest, or activity records).

Key Responsibilities:
- Stores geographic reference points extracted from GPX data.
- Persists elevation context for spatial analysis.
- Uses PostGIS for accurate geospatial querying.
- Designed as a reusable base for GPX-aware domain models.
"""

# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.contrib.gis.db import models


# Base GPX Localization model class:
class BaseGpxLocalizationModel(BaseModel):
    """
    Abstract base model for GPX-derived localization data.

    This model encapsulates spatial reference information obtained
    from GPX files, such as geographic coordinates and elevation.
    It is intended to be inherited by models that require precise
    geolocation context without embedding full GPX track data.
    """

    class Meta:
        verbose_name = 'GPX Localization'
        verbose_name_plural = 'GPX Localizations'
        abstract = True
    
    # Geographic reference point derived from GPX:
    location = models.PointField(
        geography=True,
        srid=4326,
        verbose_name='GPX Location (WGS84)',
        help_text=(
            'Primary geographic reference point derived from the GPX '
            'track, stored as a PostGIS point in WGS84 coordinates.'
        ),
        blank=True,
        null=True,
    )

    # Elevation at the given GPX location:
    elevation = models.IntegerField(
        verbose_name='GPX Elevation (m a.s.l.)',
        help_text=(
            'Elevation in meters above sea level at the given '
            'GPX-derived location.'
        ),
        blank=True,
        null=True,
    )
