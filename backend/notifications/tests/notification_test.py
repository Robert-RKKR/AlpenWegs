# AlpenWegs import:
from notifications.ashared.notifications.consumers import NotificationConsumer

# Python import:
from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer
from django.test import override_settings
from channels.routing import URLRouter
from django.urls import re_path
import pytest

# Routing for test:
application = URLRouter([
    re_path(r'ws/notifications/$', NotificationConsumer.as_asgi()),
])


@pytest.mark.asyncio
@override_settings(CHANNEL_LAYERS={
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
})
async def test_connect_and_ping():
    """
    Test that connection works and ping returns pong.
    """

    # Create a WebSocket communicator:
    communicator = WebsocketCommunicator(
        application, '/ws/notifications/'
    )
    connected, _ = await communicator.connect()
    # Check that the connection was successful:
    assert connected

    # Send ping and check response:
    await communicator.send_json_to({'action': 'ping'})
    response = await communicator.receive_json_from()
    assert response == {'action': 'pong'}

    # Disconnect the WebSocket:
    await communicator.disconnect()


@pytest.mark.asyncio
@override_settings(CHANNEL_LAYERS={
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
})
async def test_subscribe_and_receive_notification():
    """
    Test that a user can subscribe to a notification
    group and receive notifications.
    """

    # Create a WebSocket communicator:
    communicator = WebsocketCommunicator(
        application, '/ws/notifications/'
    )
    connected, _ = await communicator.connect()
    # Check that the connection was successful:
    assert connected

    # Subscribe to 'system' group:
    await communicator.send_json_to(
        {
            'action': 'subscribe',
            'group': 'system'
        }
    )
    # Check that the subscription was successful:
    response = await communicator.receive_json_from()
    # Check that the response is as expected
    assert response == {
        'action': 'subscribed',
        'group': 'system'
    }

    # Get channel layer directly:
    channel_layer = get_channel_layer()

    # Send a test message to the group:
    await channel_layer.group_send("system", {
        'type': 'send_collect',
        'event': 'test_event',
        'payload': {'message': 'hello world'}
    })

    # Receive the event and check the payload:
    response = await communicator.receive_json_from()
    assert response['event'] == 'test_event'
    assert response['payload']['message'] == 'hello world'
    
    # Disconnect the WebSocket:
    await communicator.disconnect()
