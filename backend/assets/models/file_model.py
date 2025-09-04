# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel

# Django import:
from django.db import models

# File Model class:
class FileModel(
    BaseIdentificationModel,
    BaseTimestampModel,
    BaseCreatorModel,
):
    """
    Model for storing file-related data in the application.

    This model handles essential file information like type, path, and format.
    It is designed for general file storage purposes across the application.
    """

    class Meta:

        # Model name values:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    # File Information:
    file = models.FileField(
        upload_to='files/',
        verbose_name='File Path',
        help_text='Path where the file is stored.',
    )
    format = models.CharField(
        max_length=32,
        verbose_name='File Format',
        help_text='Format of the file, e.g., pdf, gpx, txt, etc.',
    )
