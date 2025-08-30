# Rest framework import:
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status

# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import ValidationAPIException
from alpenwegs.ashared.api.base_exceptions import NotFoundAPIException
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Django import:
from django.core.exceptions import ValidationError


class BaseUpdateModelMixin(BaseMixin, UpdateModelMixin):
    """
    Mixin class to update a model instance.
    """

    def _call_update(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        # Update method:
        partial = kwargs.pop('partial', False)
        
        try: # Try to collect object instance:
            instance = self.get_object()
        
        except:
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
        
        else:
            # Collect serializer:
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            
            try:
                # Validate serializer:
                serializer.is_valid(raise_exception=True)
            
            except (ValidationError, RestValidationError) as exception:
                # Define error details list:
                error_details = []
                
                # Iterate over validation errors items to collect details:
                for field, field_errors in exception.get_full_details().items():
                    # Iterate over field errors to collect details:
                    for error in field_errors:
                        # Collect error details:
                        error_details.append({
                            'error_field': field,
                            'error_message': error.get(
                                'message',
                                'The provided data are invalid.'
                            ),
                            'error_code': error.get(
                                'code', 'validation_error'
                            ),
                        })
                
                # Raise validation API exception with collected details:
                raise ValidationAPIException(
                    error_message='The provided data are invalid.',
                    error_details=error_details,
                )
            
            else:
                # Save serializer:
                instance = serializer.save()
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
                
                # Return HTTP response 200 Object was updated:
                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK,
                )

    def update(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:
        """
        Update existing model instance.
        """


        return self._call_update(
            request=request,
            *args,
            **kwargs,
        )
