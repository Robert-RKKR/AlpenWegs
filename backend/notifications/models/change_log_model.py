# AlpenWeg import:
from alpenwegs.ashared.models.representation_model import ObjectRepresentationModel
from alpenwegs.ashared.constants.action_type import ActionTypeChoices

# AlpenWeg application import:
from profiles.models.user_model import UserModel

# Django models import:
from django.db import models


# Change model class:
class ChangeLogModel(
    ObjectRepresentationModel,
):

    class Meta:
        
        # Model name values:
        verbose_name = 'Change'
        verbose_name_plural = 'Changes'

        # Default ordering:
        ordering = ['-timestamp']
    
    # Model data time information:
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        help_text='The date and time when the change was created. This field '
            'automatically records the exact moment when the change '
            'entry is added to the log.',
        auto_now_add=True,
    )

    # Member information:
    member = models.ForeignKey(
        UserModel,
        verbose_name='Member',
        help_text='The member responsible for the change. This field '
            'links to the member who performed the action, '
            'providing accountability and traceability.',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # Change details:
    action_type = models.IntegerField(
        verbose_name='Type of action',
        help_text='The type of action that was performed on the object. This '
            'could include actions such as creation, modification, or '
            'deletion of records. The choices are defined in the '
            'ActionTypeChoices constant.',
        choices=ActionTypeChoices.choices,
        default=0,
    )
    after = models.JSONField(
        verbose_name='JSON object representation after change',
        help_text='The JSON representation of the object after the changes '
            'were made and saved to the database. This provides a '
            'snapshot of the object state post-change for auditing '
            'and rollback purposes.',
        null=True,
        blank=True,
    )
