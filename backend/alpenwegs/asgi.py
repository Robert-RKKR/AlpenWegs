# Set the default Django settings module:
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alpenwegs.settings')

# Python import:
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter

# AlpenWegs import:
import notifications.routing

# Register ASGI application with routing:
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(notifications.routing.websocket_urlpatterns)
    ),
})
