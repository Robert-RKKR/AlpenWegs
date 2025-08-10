# Rest framework import:
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework.mixins import UpdateModelMixin
from rest_framework import status

# AlpenWegs import:
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Django import:
from django.core.exceptions import ValidationError


class BaseUpdateModelMixin(BaseMixin, UpdateModelMixin):
    """
    Mixin class to update a model instance.
    """
    
    def update(self, request, *args, **kwargs):

        # Update method:
        partial = kwargs.pop('partial', False)
        
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

        else: # Check if instance is root object:
            if result := self._root_object_verification(instance): return result
            # Collect serializer:
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            
            try: # Try to update object:
                # Validate serializer:
                serializer.is_valid(raise_exception=True)
            
            except ValidationError as exception:
                # Define error code:
                error_code = status.HTTP_400_BAD_REQUEST
                # Create a new log notification:
                self._log_api_call(request, True, error_code)
                # Return HTTP response 400 - Bad request:
                return self._return_api_error(
                    error_code, 'ValidationError',
                    exception.message)
            
            except RestValidationError as exception:
                # Define error code:
                error_code = status.HTTP_400_BAD_REQUEST
                # Create a new log notification:
                self._log_api_call(request, True, error_code)
                # Return HTTP response 400 - Bad request:
                return self._return_api_error(
                    error_code, 'ValidationError',
                    'The data provided is incorrect.',
                    self.format_validation_error(exception))
            
            else: # Save serializer:
                instance = serializer.save()
                # Create a new log notification:
                self._log_api_call(request)
                # Create a new change log notification:
                self._create_notification(
                    instance, ActionTypeChoices.UPDATE, request.user,
                    serializer, self.log_changes)
                # getattr update action:
                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, 
                    # we need to forcibly invalidate the prefetch cache
                    # on the instance.
                    instance._prefetched_objects_cache = {}
                # Return HTTP response 200 - Object was updated:
                return self._return_api_response(
                    status.HTTP_200_OK,
                    serializer.data)
