"""
Abstract Base Model for object representation
---------------------------------------------

This abstract base model provides a standardized way to store metadata 
about another object in the App. It captures key details such as the 
application name, model name and primary key to represent model and a
human-readable representation of specific model object. This structure
is useful for creating generic references to objects across different
applications and models, enabling features like logging, change tracking,
or linking related data without requiring direct foreign keys.

Intended for inheritance by models that need to store consistent 
references to other objects.
"""

# AlpenWegs import:
from alpenwegs.ashared.models.base_model import BaseModel

# Django import:
from django.db import models


# Object representation model class:
class ObjectRepresentationModel(
    BaseModel, 
):
    """
    Abstract base class for storing standardized references to other
    objects in the system. Includes fields for identifying the object's
    originating application, model type, unique identifier, and a
    human-readable label.
    """

    class Meta:

        # Model name values:
        verbose_name = 'Base Object Representation Model'
        verbose_name_plural = 'Base Object Representation Models'

        # Abstract class value:
        abstract = True

    # Information about correlated object:
    app_name = models.CharField(
        verbose_name='Object application name',
        help_text='The name of the application that this object '
            'belongs to. This helps in identifying the '
            'application context of the object.',
        max_length=64,
        null=True,
        blank=True,
    )
    model_name = models.CharField(
        verbose_name='Object model name',
        help_text='The name of the model that this object '
            'is an instance of. This helps in identifying '
            'the type of the object.',
        max_length=64,
        null=True,
        blank=True,
    )
    object_id = models.CharField(
        verbose_name='Object PK number',
        help_text='The primary key (PK) number of the '
            'correlated object. This is a unique identifier '
            'for the object within its model.',
        max_length=64,
        null=True,
        blank=True,
    )
    object_repr = models.CharField(
        verbose_name='Object representation',
        help_text='A string representation of the object. '
            'This provides a human-readable description '
            'or identifier of the object.',
        max_length=128,
        null=True,
        blank=True,
    )

    #=================================================================
    # Object representation:
    #=================================================================
    def object_representation(self) -> str:
        """
        AlpenWeg model object representation:
        """

        # Return object representation:
        return self.object_repr
