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

        # Model name values:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

        # Disable default Django permissions:
        default_permissions = ()

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_photomodel', 'Can change own photos'),
            ('change_all_photomodel', 'Can change all photos'),
            ('delete_own_photomodel', 'Can delete own photos'),
            ('delete_all_photomodel', 'Can delete all photos'),
            ('view_own_photomodel', 'Can view own photos'),
            ('view_all_photomodel', 'Can view all photos'),
            ('add_own_photomodel', 'Can add own photos'),
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
