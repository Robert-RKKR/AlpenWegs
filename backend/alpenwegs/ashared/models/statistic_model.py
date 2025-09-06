"""
Abstract Base Model for Tracking object metrics
-------------------------------------------

This abstract model provides a standardized foundation for tracking 
user interactions across various entities, such as routes, events, 
and other trackable objects.

Captured engagement metrics include:
- Comments: The number of user-submitted discussions or feedback.
- Visits: The total number of views or accesses.
- Likes: User endorsements reflecting popularity.
- Downloads: Total number of times the object has been downloaded.

Designed for extensibility, this model should be inherited by 
specific models that require detailed statistical tracking to analyze 
user activity and engagement patterns effectively.
"""

# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.db import models


# Base Statistic model class:
class BaseStatisticModel(
    BaseModel, 
):
    """
    An abstract base model that tracks engagement metrics for different entities.
    This includes user interactions such as comments, visits, likes,
    accomplishments, and downloads.
    
    This model is intended to be inherited by concrete models that
    represent entities requiring statistical tracking.
    """

    class Meta:
        
        # Model name values:
        verbose_name = 'Base Statistic Model'
        verbose_name_plural = 'Base Statistic Models'
        
        # Abstract class value:
        abstract = True

    # Statistical fields:
    comment_count = models.BigIntegerField(
        verbose_name='Number of Comments',
        help_text='Total count of user-submitted comments on this object.',
        blank=False,
        null=False,
        default=0,
    )
    visit_count = models.BigIntegerField(
        verbose_name='Visit Count',
        help_text='Number of times this object has been visited by users.',
        blank=False,
        null=False,
        default=0,
    )
    download_count = models.BigIntegerField(
        verbose_name='Download Count',
        help_text='Total number of times the object has been downloaded.',
        blank=False,
        null=False,
        default=0,
    )
