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
# from assets.models.file_model import FileModel

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
    # gpx_data = models.ForeignKey(
    #     FileModel,
    #     verbose_name='GPX Data',
    #     help_text='GPX data file.',
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    # )
    geojson = models.JSONField(
        verbose_name='Route GeoJSON Data',
        help_text='GeoJSON representation of the route path. '
        'Created based on provided GPX file.',
        blank=True,
        null=True,
    )

    # Route GPX statistic metrics:
    duration = models.FloatField(
        verbose_name='Estimated Duration',
        help_text='User estimated total time required to complete '
        'the route, measured in hours. This estimate considers '
        'the user\'s predicted hiking pace along with elevation '
        'changes but may still be influenced by factors such '
        'as weather conditions and trail difficulty.',
        blank=True,
        null=True,
    )
    distance = models.FloatField(
        verbose_name='Route Distance',
        help_text='The total length of the route, measured in '
        'kilometres. This includes the full distance from '
        'start to finish, including both flat and uphill sections.',
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
        help_text='Maximum altitude reached along the route, '
        'measured in meters above sea level.',
        blank=True,
        null=True,
    )
    lowest_elevation = models.FloatField(
        verbose_name='Lowest Elevation',
        help_text='Minimum altitude encountered along the route, '
        'measured in meters above sea level.',
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
    track_types = models.JSONField(
        verbose_name='Track Types',
        help_text='JSON structure describing the types of terrain.',
        blank=True,
        null=True,
    )

    # GPX graphs:
    elevation_graph = models.JSONField(
        verbose_name='Elevation Graph',
        help_text='Xxx.',
        blank=True,
        null=True,
    )
