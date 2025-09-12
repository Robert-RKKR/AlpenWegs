# Django import:
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework.mixins import UpdateModelMixin
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status

# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import ValidationAPIException
from alpenwegs.ashared.api.base_exceptions import NotFoundAPIException
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin


class BaseUpdateModelMixin(
    BaseMixin,
    UpdateModelMixin,
):
    """
    Mixin class to update a model instance.
    """

    def _call_update(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        # Collect user from request:
        user = getattr(request, 'user', False)

        # Update method:
        partial = kwargs.pop('partial', False)
        # Collect object instance:
        instance = self.get_object()
        
        # Collect serializer:
        serializer = self._get_serializer(
            instance,
            serializer_name='detailed',
            data=request.data,
            partial=partial
        )
        
        # Add creator to serializer data if available:
        serializer.save(creator=user)
        # Validate serializer:
        serializer.is_valid(raise_exception=True)
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
        
        # Return (200 HTTP - Ok) response:
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

        try:
            # Try to update existing instance:
            return self._call_update(
                request=request,
                *args,
                **kwargs,
            )
        
        # Return (400 HTTP - Bad Request) response:
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
