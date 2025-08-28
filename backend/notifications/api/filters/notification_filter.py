# AlpenWegs application import:
from notifications.models.notification_model import NotificationModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Notification Model filter class:
class NotificationFilter(BaseFilter):

    class Meta:

        model = NotificationModel
        fields = {
            # Base notification data:
            'timestamp': ['exact', 'icontains', 'lt', 'gt'],
            'severity': ['exact', 'icontains', 'lt', 'gt'],
            'task_id': ['exact', 'icontains'],
        }
