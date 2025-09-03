# Application import:
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel

# Django import:
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission
from django.db import models


# Group model class:
class GroupModel(
    BaseTimestampModel,
):

    class Meta:

        # Model name values:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

        # Model constraints:
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='uniq_group_name',
            )
        ]

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Admin':  ['view', 'add', 'change', 'delete'],
    }

    # Group identification:
    name = models.CharField(
        verbose_name=_('Group name'),
        help_text=_('The unique name that identifies this group.'),
        max_length=150,
        unique=True,
    )

    # Group permissions:
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('Permissions'),
        help_text=_(
            'The permissions granted to this group. '
            'Users assigned to this group automatically inherit these.'
        ),
        blank=True,
    )

    #=================================================================
    # Object representation:
    #=================================================================
    def representation(self):
        """
        Collect group object representation:
        """

        # Return group object representation:
        return self.name
