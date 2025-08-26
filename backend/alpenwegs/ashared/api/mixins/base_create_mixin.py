# Rest framework import:
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status

# AlpenWegs import:
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin


# Base mixins custom classes:
class BaseCreateModelMixin(BaseMixin, CreateModelMixin):
    """
    Mixin class to create a model instance.
    """

    def create(self, request, *args, **kwargs):

        # Collect a new serializer:
        serializer = self.get_serializer(data=request.data)
        # Validate created serializer:
        serializer.is_valid(raise_exception=True)
        # Save a new instance based on validated serializer data:
        instance = serializer.save()

        # Create change log notification:
        self._create_notification(
            action=ActionTypeChoices.CREATE,
            log_changes=self.log_changes,
            serializer=serializer,
            member=request.user,
            instance=instance,
        )

        # Return HTTP response 201 object was created:
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )
