"""
Abstract GPX Track Model for Collecting Extended GPX Activity Data
------------------------------------------------------------------

This abstract model extends the Base GPX Model by incorporating
advanced, user-specific GPX activity metrics. It is designed for
handling detailed performance data derived from recorded GPX tracks,
such as heart rate, speed, movement analysis, and environmental
conditions.

Key Features:
- Extends the basic GPX data model with additional activity-related
    statistics (e.g., average speed, heart rate, moving time).
- Stores information about environmental context such as weather
    conditions and temperature.
- Provides enhanced support for performance and endurance tracking.
- Designed to be inherited by models that represent recorded
    user activities or performance-based route data.
"""

# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.db import models


# Base GPX model class:
class BaseGpxTrackModel(
    BaseModel,
):
    """
    Abstract base class extending BaseGpxModel to include detailed
    user activity and performance data derived from GPX track files.

    This class provides enhanced metrics such as speed, heart rate,
    and movement-based statistics that reflect a user's actual
    recorded activity on a given route or section.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base GPX Track Model'
        verbose_name_plural = 'Base GPX Track Models'

        # Abstract class value:
        abstract = True

    class Meta:
        verbose_name = 'Base GPX Track Model'
        verbose_name_plural = 'Base GPX Track Models'
        abstract = True

    # Time-related metrics:
    start_time = models.DateTimeField(
        verbose_name='Track Start Time',
        help_text='Timestamp marking the start of the recorded activity.',
        blank=True,
        null=True,
    )
    end_time = models.DateTimeField(
        verbose_name='Track End Time',
        help_text='Timestamp marking the end of the recorded activity.',
        blank=True,
        null=True,
    )
    moving_time = models.FloatField(
        verbose_name='Moving Time (hours)',
        help_text='Total time spent moving, excluding pauses, in hours.',
        blank=True,
        null=True,
    )
    total_time = models.FloatField(
        verbose_name='Total Time (hours)',
        help_text='Overall duration of the activity including pauses, in hours.',
        blank=True,
        null=True,
    )

    # Speed metrics:
    average_speed = models.FloatField(
        verbose_name='Average Speed (km/h)',
        help_text='Average speed over the full activity duration.',
        blank=True,
        null=True,
    )
    maximum_speed = models.FloatField(
        verbose_name='Maximum Speed (km/h)',
        help_text='Highest recorded speed during the activity.',
        blank=True,
        null=True,
    )
    minimum_speed = models.FloatField(
        verbose_name='Minimum Speed (km/h)',
        help_text='Lowest recorded speed during the activity.',
        blank=True,
        null=True,
    )

    # Heart rate metrics:
    average_heart_rate = models.FloatField(
        verbose_name='Average Heart Rate (bpm)',
        help_text='Average heart rate measured over the duration of the activity.',
        blank=True,
        null=True,
    )
    maximum_heart_rate = models.FloatField(
        verbose_name='Maximum Heart Rate (bpm)',
        help_text='Highest heart rate recorded during the activity.',
        blank=True,
        null=True,
    )
    minimum_heart_rate = models.FloatField(
        verbose_name='Minimum Heart Rate (bpm)',
        help_text='Lowest heart rate recorded during the activity.',
        blank=True,
        null=True,
    )

    # Energy and performance:
    calories_burned = models.FloatField(
        verbose_name='Calories Burned (kcal)',
        help_text='Estimated total energy expenditure during the activity.',
        blank=True,
        null=True,
    )
    steps_count = models.IntegerField(
        verbose_name='Steps Count',
        help_text='Total number of steps taken during the activity (if available).',
        blank=True,
        null=True,
    )

    # Additional environmental and contextual data:
    weather_conditions = models.CharField(
        verbose_name='Weather Conditions',
        help_text='General description of weather conditions (e.g., sunny, foggy, rainy).',
        max_length=256,
        blank=True,
        null=True,
    )
    temperature_average = models.FloatField(
        verbose_name='Average Temperature (°C)',
        help_text='Average ambient temperature during the activity.',
        blank=True,
        null=True,
    )
    equipment_used = models.CharField(
        verbose_name='Equipment Used',
        help_text='Optional description of equipment used, e.g., boots, poles, bike type.',
        max_length=512,
        blank=True,
        null=True,
    )

    # Motion and elevation data extensions:
    moving_ratio = models.FloatField(
        verbose_name='Moving Ratio (%)',
        help_text='Ratio between moving time and total time (in percent).',
        blank=True,
        null=True,
    )
    pace_average = models.FloatField(
        verbose_name='Average Pace (min/km)',
        help_text='Average pace calculated as minutes per kilometer.',
        blank=True,
        null=True,
    )
    pace_best = models.FloatField(
        verbose_name='Best Pace (min/km)',
        help_text='Best recorded pace for a single segment.',
        blank=True,
        null=True,
    )
