# AlpenWegs import:
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel

# Django import:
from django.db import models


# Object representation model class:
class ObjectRepresentationModel(
    BaseTimestampModel, 
):

    class Meta:

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

    # object representation:
    def object_representation(self) -> str:
        """
        AlpenWeg model object representation:
        """

        # Return object representation:
        return self.object_repr
