# Python library import:
from celery import Celery
import os

# Set the default Django settings module for the 'celery' program:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alpenwegs.settings')
app = Celery('alpenwegs')

# Celery settings are in settings.py using a `CELERY_` prefix:
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs:
app.autodiscover_tasks()

# Manually discover tasks:
# app.autodiscover_tasks(['dashboard.tasks.collecting_system_data_task'])

# Change default queue name:
app.conf.task_default_queue = 'default'
