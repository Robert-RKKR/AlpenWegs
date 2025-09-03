"""
Abstract Base Model for Accomplishments
---------------------------------------

This abstract base model standardizes how objects in the system track 
user accomplishments. It defines a many-to-many relationship to users 
who have accomplished or completed the object and maintains a counter.

Typical use cases include:
- Routes or challenges completed by users.
- Achievements or milestones unlocked.
- Statistical reporting of completion counts.

Intended for inheritance by models that need consistent accomplishment 
tracking functionality across the application.
"""

# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.db import models


# Base Accomplished model class:
class BaseAccomplishedModel(
    BaseModel, 
):
    """
    Abstract base class for tracking user accomplishments of a given 
    object. Includes fields for linking accomplished users and storing 
    the total number of completions.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base %(class)s to User Accomplished Model'
        verbose_name_plural = 'Base %(class)s to User Accomplished Models'

        # Abstract class value:
        abstract = True

    # Model Many-to-Many Relationships with User Model:
    users_accomplished = models.ManyToManyField(
        'profiles.UserModel',
        related_name='%(class)s_users_accomplished',
        verbose_name='Users Accomplished',
        help_text='Users who have accomplished or completed this %(class)s. '
            'Allows queries of which members completed a %(class)s.'
    )

    # Statistic Information:
    accomplished_count = models.BigIntegerField(
        verbose_name='Accomplished Count',
        help_text='Total number of users who have accomplished this %(class)s. '
            'This field improves performance and should be kept in sync with '
            '`users_accomplished` relations between %(class)s and UserModel.',
        default=0,
    )
