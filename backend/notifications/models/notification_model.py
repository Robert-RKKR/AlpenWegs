# AlpenWeg import:
from alpenwegs.ashared.constants.notification import SeverityChoices
from alpenwegs.ashared.models.base_model import BaseModel

# Django models import:
from django.db import models


# Notification model class:
class NotificationModel(
    BaseModel,
):

    class Meta:
        
        # Model name values:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': ['view'],
        'Author': ['view'],
        'Admin':  ['view'],
    }
    
    # Base notification data:
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        help_text='The date and time when the notification was created. '
            'This field is automatically populated when the '
            'notification is created.',
        auto_now_add=True,
    )
    severity = models.IntegerField(
        verbose_name='Severity level',
        help_text='The severity level of the notification. Indicates the '
            'importance or urgency of the notification.',
        choices=SeverityChoices.choices,
        default=0,
    )
    task_id = models.CharField(
        verbose_name='Task ID',
        help_text='The unique identifier of the task associated with this '
            'notification. Helps in tracking and correlating '
            'notifications to specific tasks.',
        max_length=64,
        null=True,
        blank=True,
    )
    message = models.CharField(
        verbose_name='Message',
        help_text='The notification message detailing the event or action. '
            'This message provides information about the notification. '
            'The message must be between 1 and 1024 characters long.',
        max_length=1024,
        error_messages={
            'invalid': 'Enter a valid notification message. It must '
                'contain between 1 and 1024 characters.',
        },
    )
    url = models.CharField(
        verbose_name='URL',
        help_text='The URL to the object related to this notification. '
            'This can be used to provide a direct link to the relevant '
            'object or page within the application.',
        max_length=256,
        null=True,
        blank=True,
    )

    # object representation:
    def object_representation(self) -> str:
        """
        AlpenWeg model object representation:
        """

        # Return object representation:
        return str(self.message)
