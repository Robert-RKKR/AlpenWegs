# Rest framework import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import status

# AlpenWegs import:
from alpenwegs.ashared.constants.notification import ApplicationChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# AlpenWegs application import:
from notification.ashared import Notification
from notification.ashared import Logger

# Python import:
import uuid

# Init API notification:
notification = Notification(
    'API', channel_name='objects_notifications')
task_id = str(uuid.uuid4())
logger = Logger(ApplicationChoices.API, task_id)


class BaseRetrieveModelMixin(BaseMixin, RetrieveModelMixin):
    """
    Mixin class to retrieve a model instance.
    """
    
    def _call_retrieve(self, request, *args, **kwargs):

        # Collect instance:
        instance = self.get_object()
        # Collect serializer:
        serializer = self.get_serializer(instance)
        
        # Return HTTP response 200 - Object was retrieve:
        return self._return_api_response(
            status.HTTP_200_OK, serializer.data)

    def retrieve(self, request, *args, **kwargs):

        try: # Try to make a nwe API GET - Retrieve call:
            response = self._call_retrieve(request, *args, **kwargs)
        
        except: # Define error code:
            error_code = status.HTTP_404_NOT_FOUND
            # Create a new log notification:
            self._log_api_call(request, True, error_code)
            # Return HTTP response 404 - Not found:
            return self._return_api_error(
                error_code, 'NotFoundError',
                'The object in question has not been found.')
        
        else: # Create a new log notification:
            self._log_api_call(request)
            # Return collected response:
            return response
