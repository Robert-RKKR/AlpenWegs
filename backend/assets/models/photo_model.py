# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel

# Django import:
from django.db import models


# File Model class:
class PhotoModel(
    BaseIdentificationModel,
    BaseTimestampModel,
    BaseCreatorModel,
):
    """
    Model for storing photo-related data in the application.

    This model handles essential photo information like type, path, and format.
    It is specifically designed for photo file management.
    """

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    # Photo Many-to-many relationships:
    sections = models.ManyToManyField(
        'explorers.SectionModel',
        through='explorers.SectionToPhotoModel',
        related_name='photo_routes',
        verbose_name='Associated Routes.',
    )

    # Photo Information:
    path = models.ImageField(
        upload_to='photos/',
        verbose_name='Photo Path',
        help_text='Path where the photo is stored.',
    )
    format = models.CharField(
        max_length=32,
        verbose_name='Photo Format',
        help_text='Format of the photo, e.g., jpg, png, etc.',
    )
