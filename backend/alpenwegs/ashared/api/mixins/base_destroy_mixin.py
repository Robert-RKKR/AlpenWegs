# Rest framework import:
from rest_framework.mixins import DestroyModelMixin
from rest_framework import status

# AlpenWegs import:
from alpenwegs.ashared.constants.notification import ApplicationChoices
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# AlpenWegs application import:
from notification.object_collector import collect_object_data
from notification.changer import log_change
from notification.ashared import Notification
from notification.ashared import Logger

# Django import:
from django.db.models import ProtectedError

# Python import:
import copy
import uuid

# Init API notification:
notification = Notification(
    'API', channel_name='objects_notifications')
task_id = str(uuid.uuid4())
logger = Logger(ApplicationChoices.API, task_id)



class BaseDestroyModelMixin(BaseMixin, DestroyModelMixin):
    """
    Mixin class to destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):

        try: # Try to collect object instance:
            instance = self.get_object()
        
        except: # Define error code:
            error_code = status.HTTP_404_NOT_FOUND
            # Create a new log notification:
            self._log_api_call(request, True, error_code)
            # Return HTTP response 404 - Not found:
            return self._return_api_error(
                error_code, 'Not Found',
                'The object in question has not been found.')

        else: # Create a new log notification:
            # Copy instance:
            copy_instance = copy.copy(instance)
            # Check if instance is root object:
            if result := self._root_object_verification(instance): return result
            
            try: # Try to delete provided instance:
                self.perform_destroy(instance)
            
            except ProtectedError as exception:
                # Define error code:
                error_code = status.HTTP_405_METHOD_NOT_ALLOWED
                # Create a new log notification:
                self._log_api_call(request, True, error_code)
                # Iterate thru all related objects:
                related_objects = [collect_object_data(obj) for
                    obj in exception.protected_objects]
                # Return HTTP response 405 - Not Allowed:
                return self._return_api_error(
                    error_code, 'NotAllowed',
                    str(exception.args), {'related_objects': related_objects})
            
            else: # Create a new log notification:
                self._log_api_call(request)
                # Create a new change log notification:
                self._create_notification(
                    copy_instance, ActionTypeChoices.DELETE, request.user,
                    False, self.log_changes)
                # Return 204 HTTP response if object was deleted:
                return self._return_api_response(
                    status.HTTP_204_NO_CONTENT, [], False,
                    f'Object {instance} has been successfully deleted.')
