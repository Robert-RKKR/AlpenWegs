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

        # Disable default Django permissions:
        default_permissions = ()

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_filemodel', 'Can change own files'),
            ('change_all_filemodel', 'Can change all files'),
            ('delete_own_filemodel', 'Can delete own files'),
            ('delete_all_filemodel', 'Can delete all files'),
            ('view_own_filemodel', 'Can view own files'),
            ('view_all_filemodel', 'Can view all files'),
            ('add_own_filemodel', 'Can add own files'),
        ]

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own',
        ],
        'Author': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own',
        ],
        'Admin':  [
            'change_all',
            'change_own',
            'delete_all',
            'delete_own',
            'view_all',
            'view_own',
            'add_own',
        ],
    }

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
