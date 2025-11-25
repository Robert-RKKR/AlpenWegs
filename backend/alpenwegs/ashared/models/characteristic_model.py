"""
Abstract Base Model for Route Characteristics
---------------------------------------------

This abstract base model provides a standardized way to store 
characteristics and requirements associated with routes and trips.
It includes difficulty ratings, stamina and experience 
requirements, risk descriptions, and seasonal availability.

Typical use cases include:
- Hiking, climbing, biking, or other outdoor routes.
- Classifying routes by difficulty, risk, and suitability.
- Providing guidance for users to assess their readiness 
  and plan trips safely.

Intended for inheritance by models that represent routes or 
other entities that require standardized metadata on difficulty 
and seasonal conditions.
"""

# AlpenWegs import:
from alpenwegs.ashared.constants.season_category import SeasonChoices
from alpenwegs.ashared.constants.season_category import MonthChoices
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.db import models


# Base Characteristic Model class:
class BaseCharacteristicModel(
    BaseModel,
):
    """
    Abstract base class for storing difficulty levels, risk assessments, 
    stamina/experience requirements, and seasonal availability of routes.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Characteristic Model'
        verbose_name_plural = 'Base Characteristic Models'

        # Abstract class value:
        abstract = True

    # Characteristics values:
    estimated_duration = models.FloatField(
        verbose_name='Estimated Duration',
        help_text='User estimated total time required to complete '
            'the route, measured in hours. This estimate considers '
            'the user\'s predicted hiking pace along with elevation '
            'changes but may still be influenced by factors such '
            'as weather conditions and trail difficulty.',
        blank=True,
        null=True,
    )
    difficulty = models.CharField(
        verbose_name='General Difficulty Level',
        help_text='Overall difficulty level of the route. Options '
            'include: Easy, Moderate, Difficult, Very Difficult, '
            'and Extremely Difficult routes.',
        max_length=32,
        blank=True,
        null=True,
    )
    stamina_requirement = models.CharField(
        verbose_name='Stamina Requirement',
        help_text='Level of stamina required to complete the route.',
        max_length=32,
        blank=True,
        null=True,
    )
    experience_requirement = models.CharField(
        verbose_name='Experience Requirement',
        help_text='Level of experience required to safely '
            'complete the entire route.',
        max_length=32,
        blank=True,
        null=True,
    )
    potential_risk_requirement = models.CharField(
        verbose_name='Risk Requirement',
        help_text='Potential risks associated with this route.',
        max_length=32,
        blank=True,
        null=True,
    )
    potential_risk_description = models.CharField(
        verbose_name='Risk Description',
        help_text='Detailed description of possible hazards along the route.',
        max_length=8192,
        blank=True,
        null=True,
    )
    family_friendly = models.BooleanField(
        verbose_name='Family Friendly',
        help_text='Indicates if the route is suitable for families.',
        blank=True,
        null=True,
    )

    # Seasonal values:
    best_seasons = models.IntegerField(
        choices=SeasonChoices.choices,
        verbose_name='Best Seasons',
        help_text='Best seasons for hiking this route.',
        default=SeasonChoices.SUMMER,
    )
    best_months = models.IntegerField(
        choices=MonthChoices.choices,
        verbose_name='Best Months',
        help_text='List of best months to complete this route.',
        default=MonthChoices.JANUARY,
    )
    winter_season = models.BooleanField(
        verbose_name='Available in Winter',
        help_text='Indicates if the route is accessible in winter.',
        blank=True,
        null=True,
    )
    summer_season = models.BooleanField(
        verbose_name='Available in Summer',
        help_text='Indicates if the route is accessible in summer.',
        blank=True,
        null=True,
    )
