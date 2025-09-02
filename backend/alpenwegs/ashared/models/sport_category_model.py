"""
Abstract Base Model for Sport Categories
----------------------------------------

This abstract base model provides a standardized way to associate an 
object with a sport category (e.g., hiking, via ferrata, climbing, 
biking) and an optional difficulty level specific to that category.

It is designed to be inherited by models that need to be categorized 
by sport type and evaluated by a grading system relevant to that 
sport. For example:
- Hiking routes classified by T1-T6 difficulty levels.
- Via ferrata routes classified by K1-K6.
- Other sports with their own standardized grading scales.

Intended for inheritance by models representing sport-related 
objects that require both category identification and 
sport-specific difficulty ratings.
"""

# AlpenWegs import:
from alpenwegs.ashared.constants.sport_category_difficulty import SportCategoryDifficultyChoices
from alpenwegs.ashared.constants.sport_category import SportCategoryChoices
from .base_model import BaseModel

# Django import:
from django.db import models


# Base Sport Category Model class:
class BaseSportCategoryModel(
    BaseModel,
):
    """
    Abstract base class for associating an object with a sport 
    category and its corresponding difficulty rating.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Sport Category Model'
        verbose_name_plural = 'Base Sport Category Models'

    # Category value:
    category = models.IntegerField(
        choices=SportCategoryChoices.choices,
        verbose_name='Sport Category',
        help_text='The sport or activity associated with this '
            'object (e.g., hiking, via ferrata, climbing, biking).',
        default=SportCategoryChoices.HIKING,
    )

    # Characteristics values:
    category_specific_difficulty = models.IntegerField(
        choices=SportCategoryDifficultyChoices.choices,
        verbose_name='Difficulty Level',
        help_text='Difficulty level within the chosen sport category. '
            'Examples: T2 for hiking routes, K3 for via ferrata. '
            'This field enables precise classification of route '
            'complexity using established grading systems.',
        default=SportCategoryDifficultyChoices.T3,
    )
