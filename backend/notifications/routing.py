# AlpenWegs application import:
from notifications.ashared.notifications.consumers import NotificationConsumer

# Django import:
from django.urls import re_path

# Register notification channel:
websocket_urlpatterns = [
    re_path(r'^ws/notifications/$', NotificationConsumer.as_asgi()),
]
