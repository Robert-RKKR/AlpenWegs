"""
Abstract Base Model for Scoring System
--------------------------------------

This abstract base model provides a standardized way to represent and 
store score-based data for various objects, such as routes or events. It 
includes a `score` field that holds an average rating calculated from user 
submissions. This allows objects to have a quantifiable rating based on 
user feedback.

This model is intended to be inherited by models that require a scoring 
system.
"""

# AlpenWegs import:
from .base_model import BaseModel

# Django import:
from django.db import models


# Base Score model class:
class BaseScoreModel(
    BaseModel, 
):
    """
    An abstract model representing a universal scoring system. 
    This model provides a standardized way to store and calculate 
    ratings for different objects such as routes or events.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Score model'
        verbose_name_plural = 'Base Score models'

        # Abstract class value:
        abstract = True

    # Score model values:
    score = models.FloatField(
        verbose_name='Score',
        help_text='The overall rating score, calculated based on '
        'user ratings. Score is based on user scores, where users '
        'can rate each object from 1 to 5.',
        blank=False,
        null=False,
        default=0,
    )
