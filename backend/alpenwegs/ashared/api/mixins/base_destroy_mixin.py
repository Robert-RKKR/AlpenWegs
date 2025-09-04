# AlpenWegs application import:
from notifications.ashared.changes.collector import collect_object_data

# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import ProtectedAPIException
from alpenwegs.ashared.api.base_exceptions import NotFoundAPIException
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Django import:
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from django.db.models import ProtectedError
from django.http.response import Http404
from rest_framework import status

# Python import:
import copy


class BaseDestroyModelMixin(BaseMixin, DestroyModelMixin):
    """
    Mixin class to destroy a model instance.
    """
    
    def _call_destroy(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:
        
        # Collect object instance:
        instance = self.get_object()

        # Copy instance:
        copy_instance = copy.copy(instance)
        # Delete provided instance:
        self.perform_destroy(instance)

        # Create a new change log notification:
        self._create_notification(
            copy_instance, ActionTypeChoices.DELETE, request.user,
            False, self.log_changes)
        
        # Return (204 HTTP - No Content) response:
        return self._return_api_response(
            status.HTTP_204_NO_CONTENT, [], False,
            f'Object {instance} has been successfully deleted.'
        )

    def destroy(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:
        
        try:
            # Try to delete a single instance:
            return self._call_destroy(
                request=request,
                *args,
                **kwargs,
            )
        
        # Return (404 HTTP - Not Found) response:
        except Http404 as exception:
            # Define error details list:
            error_details = {
                'error_field': kwargs,
                'error_message': 'Item with provided PK value does not exist.',
                'error_code': 'item_not_found',
            }
            
            # Raise validation API exception with collected details:
            raise NotFoundAPIException(
                error_details=error_details,
            )
        
        # Return (409 HTTP - Conflict) response:
        except ProtectedError as exception:
            # Iterate thru all related objects:
            related_objects = [collect_object_data(obj) for
                obj in exception.protected_objects]

            # Define error details list:
            error_details = {
                'error_field': related_objects,
                'error_message': 'The item cannot be deleted because '
                    'it is protected or has related objects.',
                'error_code': 'deletion_protected',
            }

            # Raise validation API exception with collected details:
            raise ProtectedAPIException(
                error_details=error_details,
            )
