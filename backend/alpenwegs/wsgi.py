# Python library import:
import os

# Django - wsgi import:
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'wsgi' application:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alpenwegs.settings')

# Get WSGI application:
application = get_wsgi_application()
