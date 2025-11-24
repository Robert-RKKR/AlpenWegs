# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import ValidationAPIException
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.models.base_model import BaseModel
from alpenwegs.logger import logger

# AlpenWegs application import:
from notifications.ashared.notifications.notification import Notification
from notifications.ashared.changes.collector import collect_object_data
from notifications.ashared.changes.changer import log_change
from profiles.models.user_model import UserModel

# Python import:
from django.core.exceptions import ImproperlyConfigured
import redis


# Base Mixin class:
class BaseMixin():

    def _get_serializer_class(self,
        serializer_name: str,
    ):
        """
        Collect serializer class using its name.
        """
        
        # Collect serializer class using name:
        serializer = getattr(
            self,
            f'{serializer_name}_serializer_class',
            False,
        )
        
        # Check if serializer exists:
        if serializer:
            # Return serializer if exists:
            return serializer
        else:
            # Raise error if serializer does not exist:
            raise AttributeError(
                f'Serializer with name \'{serializer_name}\' has not been '
                f'defined in {self.__class__.__name__} class.'
            )
        
    def _get_serializer(self,
        *args,
        serializer_name: str = None,
        **kwargs
    ):
        """
        Custom serializer resolver.
        """

        if serializer_name:
            serializer_class = self._get_serializer_class(serializer_name)
        else:
            serializer_class = self.get_serializer_class()

        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def _create_change_notification(self,
        instance: BaseModel,
        action: ActionTypeChoices,
        user: UserModel,
        serializer: bool = False,
        create_change: bool = False,
        send_notification: bool = False,
    ) -> None:
        """
        Create a notification for object changes.
        """

        if create_change:
            # Create a new change notification:
            log_change(
                instance=instance,
                user=user,
                action=action,
            )
            
            # Collect object data:
            object_related_data = collect_object_data(instance)
            model_name = object_related_data.get('model_name', False)
            instance_representation = object_related_data.get(
                'object_representation', False)
            # Collect url:
            url = serializer.data.get('url') if serializer else None

            # Collect action representation:
            action_repr = ActionTypeChoices.value_from_int(action)

            # Check if notification should be sent:
            if send_notification:

                # Create a new notification:
                notification = Notification(
                    task_id=f'api-{action_repr}',
                    channel_name=f'user_{user.id}',
                )

                try:
                    # Send notification:
                    notification.info(
                        f'{model_name} "{instance_representation}" '
                        f'has been {action_repr}d.',
                        url=url
                    )

                except (
                    redis.exceptions.ConnectionError,
                    redis.exceptions.TimeoutError,
                    redis.exceptions.ReadOnlyError,
                    ImproperlyConfigured
                ) as exception:

                    # Log error if notification service is unavailable:
                    logger.critical(
                        f'Notification service unavailable: {exception}'
                    )

                except Exception as exception:

                    # Log error if notification service is unavailable:
                    logger.critical(
                        f'Notification error: {exception}'
                    )
