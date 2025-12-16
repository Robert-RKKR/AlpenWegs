# Import Celery app instance:
from .celery import app as celery_app

# Indicate that Celery app is part of the package's public API:
__all__ = ("celery_app",)
