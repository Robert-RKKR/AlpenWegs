# Python import:
import pytest
import os

# If DJANGO_SETTINGS_MODULE wasn’t picked up from pytest.ini, enforce:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alpenwegs.settings')

@pytest.fixture(autouse=True)
def _channels_inmemory(settings, monkeypatch):
    """
    Use an in-memory channel layer during tests to avoid Redis writes.
    Also patch notifications broadcast to no-op so tests don’t hit Channels.
    """
    
    settings.CHANNEL_LAYERS = {
        'default': {'BACKEND': 'channels.layers.InMemoryChannelLayer'}
    }

    # Patch Notification.info() to no-op (adjust import path if different)
    try:
        from notifications.ashared.notifications.notification import Notification
        monkeypatch.setattr(Notification, 'info', lambda *a, **k: None)
    except Exception:
        # If notifications app isn’t used in some test modules, ignore
        pass

@pytest.fixture(autouse=True)
def _default_env(monkeypatch):
    """
    Set any env flags your settings expect for test runs (if applicable).
    """
    monkeypatch.setenv('ENV', 'TEST')
