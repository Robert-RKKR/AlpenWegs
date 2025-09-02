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
from django.db import models


# Base Relationship models class:
class BaseRelationshipModel(
    BaseTimestampModel, 
):
    """
    Abstract base class for relationship models that provides
    timestamping for relations models. Intended for inheritance by
    specific relationship models that link entities such as
    routes, points of interest, users, etc.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Relationship Model'
        verbose_name_plural = 'Base Relationship Models'

        # Abstract class value:
        abstract = True

    #=================================================================
    # Object representation:
    #=================================================================
    def object_representation(self) -> str:
        """
        AlpenWeg model object representation:
        """

        # Return object representation:
        return f'Position: {self.order}'


class BaseRelationshipOrderedModel(
    BaseRelationshipModel, 
):
    """
    Abstract base class for relationship models that provides
    ordering and timestamping. Intended for inheritance by
    specific relationship models that link entities such as
    routes, points of interest, users, etc.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Ordered Relationship Model'
        verbose_name_plural = 'Base Ordered Relationship Models'

        # Abstract class value:
        abstract = True

    # Relationship model values:
    position = models.IntegerField(
        verbose_name='Position',
        help_text='Manual ordering within this relationship. '
            'Use gap indexing (10,20,30).',
        default=10,
    )
