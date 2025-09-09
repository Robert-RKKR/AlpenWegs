# AlpenWegs import:
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.models.base_model import BaseModel

# AlpenWegs application import:
from notifications.ashared.notifications.notification import Notification
from notifications.ashared.changes.collector import collect_object_data
from notifications.ashared.changes.changer import log_change
from profiles.models.user_model import UserModel


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
                f'Serializer with name "{serializer_name}" has not been '
                f'defined in {self.__class__.__name__} class.'
            )

    def _create_notification(self,
        instance: BaseModel,
        action: ActionTypeChoices,
        user: UserModel,
        serializer = False,
        log_changes = False
    ) -> None:
        """
        Create a notification for object changes.
        """

        if log_changes:
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

            # Create a new notification:
            notification = Notification(
                task_id=f'api-{action_repr}',
                channel_name=f'user_{user.id}',
            )
            # Send notification:
            notification.info(f'{model_name} "{instance_representation}" '
                f'has been {action_repr}d.', url=url
            )
