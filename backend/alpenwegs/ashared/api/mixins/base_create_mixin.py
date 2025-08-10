# Rest framework import:
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework import status

# AlpenWegs import:
from alpenwegs.ashared.constants.notification import ApplicationChoices
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# AlpenWegs application import:
from notification.ashared import Notification
from notification.ashared import Logger

# Django import:
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.contrib import admin

# Python import:
import copy
import uuid

# Init API notification:
notification = Notification(
    'API', channel_name='objects_notifications')
task_id = str(uuid.uuid4())
logger = Logger(ApplicationChoices.API, task_id)


# Base mixins custom classes:
class BaseCreateModelMixin(BaseMixin, CreateModelMixin):
    """
    Mixin class to create a model instance.
    """

    def create(self, request, *args, **kwargs):

        # Collect serializer:
        serializer = self.get_serializer(data=request.data)
        
        try: # try to validate serializer:
            serializer.is_valid(raise_exception=True)
        
        except RestValidationError as error:
            # Define error code:
            error_code = status.HTTP_400_BAD_REQUEST
            # Create a new log notification:
            self._log_api_call(request, True, error_code)
            # Return HTTP response 400 - Bad request:
            return self._return_api_error(
                error_code, 'ValidationError',
                'The data provided is incorrect.',
                self.format_validation_error(error))
        
        else: # Save serializer:
            instance = serializer.save()
            # Create a new log notification:
            self._log_api_call(request)
            # Create change log notification:
            self._create_notification(
                instance, ActionTypeChoices.CREATE, request.user,
                serializer, self.log_changes)
            # Return HTTP response 201 - object was created:
            return self._return_api_response(
                status.HTTP_201_CREATED,
                serializer.data, True)
