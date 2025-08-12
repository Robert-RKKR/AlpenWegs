"""
Abstract Base Model for Timestamps tracking
------------------------------------------------------

This abstract base model is designed to automatically track the 
creation and last update timestamps for each object. The `created` 
timestamp is set when the object is first created and remains immutable, 
while the `updated` timestamp reflects the last time the object was modified.

This model is intended to be inherited by other models that require timestamp 
tracking for both object creation and modification.
"""

# Application import:
from .base_model import BaseModel

# Django import:
from django.db import models


# Base Timestamp model class:
class BaseTimestampModel(BaseModel):
    """
    An abstract base model for tracking creation and update timestamps.

    This model automatically handles `created` and `updated` timestamp fields 
    for each object. The `created` field is set when the object is first created 
    and cannot be modified. The `updated` field is automatically updated 
    every time the object is modified.

    Intended to be inherited by models that need to track:
    - The creation date and time of the object.
    - The last modification date and time of the object.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Timestamp model'
        verbose_name_plural = 'Base Timestamp models'

        # Abstract class value:
        abstract = True

    # Timestamp model values:
    created = models.DateTimeField(
        verbose_name='Created Timestamp',
        help_text='Stores the date and time when the object was '
            'firstly created. This timestamp field is automatically '
            'set when the object is created and cannot be '
            'modified after creation.',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated Timestamp',
        help_text='Records the date and time when the object was last '
            'updated. This timestamp field is automatically updated '
            'whenever the object is modified.',
        auto_now=True,
    )

    #=================================================================
    # Object representation:
    #=================================================================
    def object_representation(self) -> str:
        """
        AlpenWeg model object representation:
        """

        # Return object representation:
        return f'Created: {self.created}, Updated: {self.updated}'
