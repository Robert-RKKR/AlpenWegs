"""
Abstract Route Model for Collecting Base GPX Data
---------------------------------------------------

This abstract model serves as a foundation for handling GPX-based 
route data in the application. It stores essential geographical 
and statistical information derived from GPX files, allowing 
user to analyze routes in terms of distance, elevation, and 
difficulty.

Key Features:
- Stores GPX data and its GeoJSON representation.
- Maintains key route statistics such as distance, elevation 
  gain/loss, and estimated duration.
- Includes fields for additional data visualization, such as 
  elevation graphs.
- Designed to be extended by other models that require GPX-based 
  route processing.
"""

# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel

# AlpenWegs application import:
from assets.models.file_model import FileModel

# Django import:
from django.db import models


# Base GPX model class:
class BaseGpxModel(
    BaseModel,
):
    """
    Abstract base model for storing GPX-related route data. 

    This model provides a structured way to manage essential route 
    information, including distance, elevation, estimated duration, 
    and terrain types. It also supports visual data representations, 
    such as elevation graphs, for enhanced route analysis.

    Intended to be inherited by models requiring GPX-based route 
    storage and processing.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base GPX Model'
        verbose_name_plural = 'Base GPX Modes'

        # Abstract class value:
        abstract = True

    # Route GPX data:
    gpx_data = models.ForeignKey(
        FileModel,
        verbose_name='GPX Data',
        help_text='Stores the uploaded GPX file used to create and extract '
            'route information. It contains the raw measurement data '
            'required for distance elevation and grade analysis.',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    geojson = models.JSONField(
        verbose_name='Route GeoJSON Data',
        help_text='Stores the GeoJSON representation of the route. This data '
            'is generated from the GPX file to allow visual mapping and '
            'geographical inspection in a standard format.',
        blank=True,
        null=True,
    )

    # Route GPX statistic metrics:
    total_distance = models.FloatField(
        verbose_name='Total Distance (meters)',
        help_text='Total traversable route length computed from the '
            'GPX coordinates, including 3D distance calculation when '
            'elevation differences are present.',
        blank=True,
        null=True,
    )
    total_points = models.IntegerField(
        verbose_name='Total GPX Points',
        help_text='Total number of individual track coordinate points '
            'recorded across every track segment in the GPX dataset. '
            'Higher values indicate greater GPS sampling density.',
        blank=True,
        null=True,
    )
    elevation_gain = models.FloatField(
        verbose_name='Elevation Gain',
        help_text='Total amount of ascent measured in meters. '
            'This is the cumulative elevation gain over the '
            'entire route, adding up all the uphill sections.',
        blank=True,
        null=True,
    )
    elevation_loss = models.FloatField(
        verbose_name='Elevation Loss',
        help_text='Total amount of descent measured in meters. '
            'This is the cumulative descent over the entire route, '
            'adding up all downhill sections.',
        blank=True,
        null=True,
    )
    highest_elevation = models.FloatField(
        verbose_name='Highest Elevation',
        help_text='The highest altitude point measured along the '
            'recorded route. This metric helps determine '
            'alpine difficulty levels.',
        blank=True,
        null=True,
    )
    lowest_elevation = models.FloatField(
        verbose_name='Lowest Elevation',
        help_text='The lowest altitude point measured along the '
            'route. This value defines the minimum elevation '
            'reached during the activity.',
        blank=True,
        null=True,
    )
    average_grade = models.FloatField(
        verbose_name='Average Grade',
        help_text='The average percentage of incline over the '
            'entire route, calculated as (total elevation gain / total '
            'distance) x 100. A higher value indicates a steeper route.',
        blank=True,
        null=True,
    )
    highest_grade = models.FloatField(
        verbose_name='Maximum Grade',
        help_text='The steepest percentage climb at any point on the route. '
            'This is the most challenging section in terms of gradient.',
        blank=True,
        null=True,
    )

    # Track types:
    track_types = models.JSONField(
        verbose_name='Track Types',
        help_text='Stores descriptive information about the route '
            'terrain. This may include surface type difficulty '
            'and structure segments.',
        blank=True,
        null=True,
    )

    # GPX graphs:
    elevation_graph = models.JSONField(
        verbose_name='Elevation Graph',
        help_text='Structured dataset used to construct an elevation '
            'profile chart. Provides the height progression '
            'along the full track distance.',
        blank=True,
        null=True,
    )
