# AlpenWegs import:
from alpenwegs.ashared.constants.notification import SeverityChoices

# AlpenWeg application import:
from notifications.models.notification_model import NotificationModel

# Django imports:
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db import transaction

# Python import:
from typing import Optional


# Main Notification Class:
class Notification:

    def __init__(self,
        task_id: str,
        channel_name: str,
    ) -> None:
        """
        Initialize a notification instance.

        Args:
            task_id (str):
                The ID of the task associated with the notification.
            channel_name (str):
                The name of the channel to which the notification will be sent.
        """

        # Define base notification attributes:
        self.channel_name = channel_name
        self.task_id = task_id

    # Notification error severity method:
    def error(self,
        message: str,
        url: Optional[str] = None
    ) -> NotificationModel | None:
        """
        Send a new error notification with error severity.

        Args:
            message (str):
                The error message to send.
            url (Optional[str]):
                An optional URL associated with the notification.

        Returns (NotificationModel | None):
            The created notification or None if not sent.
        """
        
        # Return the created notification:
        return self._create_and_broadcast(
            SeverityChoices.ERROR, message, url)

    # Notification warning severity method:
    def warning(self,
        message: str,
        url: Optional[str] = None
    ) -> NotificationModel | None:
        """
        Send a new error notification with warning severity.

        Args:
            message (str):
                The error message to send.
            url (Optional[str]):
                An optional URL associated with the notification.

        Returns (NotificationModel | None):
            The created notification or None if not sent.
        """
       
        # Return the created notification:
        return self._create_and_broadcast(
            SeverityChoices.WARNING, message, url)

    # Notification info severity method:
    def info(self,
        message: str,
        url: Optional[str] = None
    ) -> NotificationModel | None:
        """
        Send a new error notification with info severity.

        Args:
            message (str):
                The error message to send.
            url (Optional[str]):
                An optional URL associated with the notification.

        Returns (NotificationModel | None):
            The created notification or None if not sent.
        """

        # Return the created notification:
        return self._create_and_broadcast(
            SeverityChoices.INFO, message, url)

    # Notification creation and broadcasting method:
    def _create_and_broadcast(self,
        severity: int,
        message: str,
        url: Optional[str] = None
    ) -> NotificationModel | None:

        # Sanitize inputs:
        message = self._clean_message(message)
        url = self._clean_url(url)

        # Create Notification model object:
        notification = NotificationModel.objects.create(
            task_id=self.task_id,
            message=message,
            severity=severity,
            object_url=url,
        )

        # Broadcast only after commit succeeds:
        def _after_commit():
            # Collect channel layer:
            channel_layer = get_channel_layer()
            if not channel_layer:
                return None

            # Prepare the event payload:
            event = {
                'timestamp': notification.timestamp.isoformat(),
                'id': str(notification.pk),
                'severity': int(severity),
                'task_id': self.task_id,
                'type': 'send_collect',
                'message': message,
                'object_url': url,
            }

            # Send the event to the appropriate channel group:
            async_to_sync(channel_layer.group_send)(self.channel_name, event)

        # Call the transaction on commit hook:
        transaction.on_commit(_after_commit)
        # Return the created notification:
        return notification

    @staticmethod
    def _clean_message(
        message: str
    ) -> str:
        
        # Check if message in not to long:
        if len(message) > 1024:
            # Truncate message and add ellipsis:
            return message[:1020] + " ..."

        # Return the non changed message:
        return message

    @staticmethod
    def _clean_url(
        url: Optional[str]
    ) -> Optional[str]:

        # Return None if URL not provided:
        if not url:
            return None
        
        # Check if URL in not to long:
        if len(url) > 256:
            # Truncate URL and add ellipsis:
            return url[:252] + " ..."
