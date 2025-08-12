"""
Abstract Base Relationship Model
-------------------------------------------------

This abstract model provides a foundational structure for managing
ordered relationships between entities. It includes a timestamp mixin
and a configurable order field, intended to be extended by specific
relationship models across the application.
"""

# AlpenWegs import:
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel

# Django import:
from django.contrib.auth.models import User
from django.db import models


# Base Relationship models class:
class BaseRelationshipModel(
    BaseTimestampModel, 
):
    """
    Abstract base class for relationship models that require
    ordering and timestamping. Intended for inheritance by
    specific relationship models that link entities such as
    routes, points of interest, users, etc.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Relationship Model'
        verbose_name_plural = 'Base Relationship Models'

        # Abstract class value:
        abstract = True

    # Relationship model values:
    order = models.IntegerField(
        verbose_name='Order',
        help_text='Defines the ordering or precedence '
            'of the relationship.',
        default=0,
    )

    #=================================================================
    # Object representation:
    #=================================================================
    def object_representation(self) -> str:
        """
        AlpenWeg model object representation:
        """

        # Return object representation:
        return f'Order: {self.order}'
