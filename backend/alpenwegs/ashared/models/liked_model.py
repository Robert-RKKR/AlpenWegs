"""
Abstract Base Model for Likes
-----------------------------

This abstract base model standardizes how objects in the system handle 
likes and user engagement. It defines a many-to-many relationship to 
users who liked the object and maintains a counter.

Typical use cases include:
- Articles, routes, or points of interest liked by users.
- Popularity tracking across different content types.
- Supporting social engagement and ranking features.

Intended for inheritance by models that require consistent "like" 
functionality across the application.
"""

# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.db import models


# Base Liked model class:
class BaseLikedModel(
    BaseModel, 
):
    """
    Abstract base class for tracking which users liked an object and 
    storing the total number of likes.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base %(class)s to User Liked Model'
        verbose_name_plural = 'Base %(class)s to User Liked Models'

        # Abstract class value:
        abstract = True

    # Model Many-to-Many Relationships with User Model:
    users_liked = models.ManyToManyField(
        'profiles.UserModel',
        related_name='%(class)s_users_liked',
        verbose_name='Users Liked',
        help_text='Users who liked this %(class)s. Used to record engagement '
            'and allow retrieval of which members expressed a positive reaction.'
    )

    # Statistic Information:
    like_count = models.BigIntegerField(
        verbose_name='Like Count',
        help_text='Total number of likes this %(class)s has received. '
            'This field is used for faster queries and should be '
            'synchronized with `users_liked` relations between '
            'Model and UserModel.',
        default=0,
    )
