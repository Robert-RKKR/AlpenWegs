# Special import on top:
from __future__ import annotations

# Python import:
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from urllib.parse import parse_qs

# AlpenWegs import:
from alpenwegs.logger import api_logger as logger


class NotificationConsumer(
    AsyncJsonWebsocketConsumer,
):
    """
    WebSocket consumer for push notifications.
    
    Expects group events with type='send_collect'
    and a JSON-serializable payload.
    """

    async def connect(self):

        # Track joined groups:
        self.groups_joined: set[str] = set()

        # Always join the default broadcast channel:
        await self._join_group('notification')

        # Per-user channel (optional)
        user = self.scope.get('user')
        if user and getattr(user, 'is_authenticated', False):
            await self._join_group(f'user_{user.id}')

        # Extra groups via query string.
        # E.g. ws://.../ws/notifications/?channels=system,ops
        raw_qs = self.scope.get('query_string', b'').decode('utf-8')
        qs = parse_qs(raw_qs)
        for name in (qs.get('channels', []) or []):
            for g in name.split(','):
                await self._join_group(g.strip())

        # Accept the WebSocket connection:
        await self.accept()

    async def disconnect(self,
        close_code: int,
    ):

        # Iterate thru all groups:
        for group in list(self.groups_joined):
            # Close the group connection:
            await self.channel_layer.group_discard(
                group, self.channel_name)

        # Clear the set of joined groups:
        self.groups_joined.clear()

    async def receive_json(self,
        content: dict,
        **kwargs: dict,
    ):

        # Handle incoming JSON messages:
        action = content.get('action')

        try:
            # Try to handle subscription actions:
            if action == 'subscribe':
                # Collect group name:
                group = str(content.get('group', '')).strip()
                # Join the group:
                await self._join_group(group)
                # Send subscription confirmation:
                await self.send_json({'action': 'subscribed', 'group': group})

            elif action == 'unsubscribe':
                # Collect group name:
                group = str(content.get('group', '')).strip()
                # Leave the group:
                await self._leave_group(group)
                # Send unsubscription confirmation:
                await self.send_json({'action': 'unsubscribed', 'group': group})

            elif action == 'ping':
                # Send pong response:
                await self.send_json({'action': 'pong'})

        except Exception as exception:
            # Log error:
            logger.error('An error occurred while processing '
                f'{action} action. Error: {exception}',
                exc_info=True
            )
            # Send error response to client:
            await self.send_json({
                'action': 'error',
                'message': f'Failed to process {action} action.'
            })

    async def send_collect(self,
        event: dict,
    ):
        """
        Handler for group_send(... {'type': 'send_collect', ...})
        We forward the event minus the Channels 'type' key.
        """

        # Convert Python dictionary into Json:
        payload = {k: v for k, v in event.items() if k != "type"}
        # Send message to channel:
        await self.send_json(payload)

    async def _join_group(self,
        name: str,
    ):

        # Validate group name:
        if not name or name in self.groups_joined:
            return None
        
        # Prevent cross-user subscription:
        if name.startswith('user_'):
            user = self.scope.get('user')
            expected = f'user_{
                getattr(user, 'id', None)}' if user and getattr(
                    user, 'is_authenticated', False) else None
            if name != expected:
                return None

        # Join the group:
        await self.channel_layer.group_add(
            name, self.channel_name)
        self.groups_joined.add(name)

    async def _leave_group(self,
        name: str
    ):

        # Validate group name:
        if name not in self.groups_joined:
            return None

        # Leave the group:
        await self.channel_layer.group_discard(
            name, self.channel_name)
        self.groups_joined.discard(name)
