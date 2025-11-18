"""
Abstract Base Model for Multi-Day Objects
-----------------------------------------

This abstract base model provides shared fields and logic for any model that
represents a multi-day outdoor activity or itinerary. It includes temporal
metadata (start/end dates, total duration) and accommodation information,
allowing consistent behaviour across both planned Trips and executed Journeys.

Intended for use by models that represent multi-day concepts, such as Trips
(planned) and Journeys (executed).
"""

# AlpenWegs import:
from alpenwegs.ashared.constants.accommodation_type import AccommodationTypeChoices
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.db import models


class BaseMultiDayModel(BaseModel):
    """
    Abstract base model providing core metadata for multi-day structures.
    This includes the temporal span (start and end dates), calculated or
    manually supplied duration, and the type of accommodation associated
    with the activity. Designed for use by both planned itineraries (Trips)
    and executed real-world experiences (Journeys).
    """

    class Meta:
        verbose_name = 'Base Multi-Day Model'
        verbose_name_plural = 'Base Multi-Day Models'
        abstract = True

    # --------------------------------------------------------
    # Multi-day temporal metadata
    # --------------------------------------------------------
    start_date = models.DateField(
        verbose_name='Start Date',
        help_text=(
            'Date when the multi-day activity began. Used for chronological '
            'ordering, seasonal analysis, weather interpretation, and linking '
            'to long-term progress or training cycles.'
        ),
        blank=True,
        null=True,
    )
    end_date = models.DateField(
        verbose_name='End Date',
        help_text=(
            'Date when the multi-day activity concluded. Together with the '
            'start date, this defines the total duration of the activity and '
            'supports automated calculation of daily structure.'
        ),
        blank=True,
        null=True,
    )
    total_days = models.IntegerField(
        verbose_name='Total Days',
        help_text=(
            'Total number of days for the multi-day activity. If not provided, '
            'the system may calculate this automatically based on start/end '
            'dates or derived information from related Tracks.'
        ),
        blank=True,
        null=True,
    )

    # --------------------------------------------------------
    # Accommodation metadata (planned or used)
    # --------------------------------------------------------
    accommodation = models.IntegerField(
        verbose_name='Accommodation Type',
        choices=AccommodationTypeChoices.choices,
        help_text=(
            'Type of accommodation associated with this multi-day activity. '
            'For planned Trips, this represents the intended lodging strategy. '
            'For executed Journeys, it reflects the actual accommodation used. '
            'Values include dormitories, private rooms, mountain huts, '
            'camping sites, bivouacs, hotels, and mixed arrangements.'
        ),
        blank=True,
        null=True,
    )
