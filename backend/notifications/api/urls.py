# AlpenWegs import:
from alpenwegs.ashared.api.base_default_router import BaseDefaultRouter

# AlpenWegs application import:
from notifications.api.views.notification_view import NotificationView
from notifications.api.views.change_log_view import ChangeLogView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-notification'

# Standard view route registration:
router.register(r'notification', NotificationView, basename='notification_model')
router.register(r'change-log', ChangeLogView, basename='change_log_model')

# Add urlpatterns:
urlpatterns = router.urls
