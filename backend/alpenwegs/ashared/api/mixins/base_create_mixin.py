# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import ValidationAPIException
from alpenwegs.ashared.constants.action_type import ActionTypeChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Rest framework import:
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status


# Base mixins custom classes:
class BaseCreateModelMixin(
    BaseMixin,
    CreateModelMixin,
):
    """
    Mixin class to create a model instance.
    """

    def _call_create(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        # Collect user from request:
        user = getattr(request, 'user', False)

        # Collect a new objet detailed serializer:
        serializer = self._get_serializer(
            serializer_name='detailed',
            data=request.data,
        )
        
        # Add creator to serializer data if available:
        serializer.save(creator=user)
        # Validate created serializer:
        serializer.is_valid(raise_exception=True)
        # Save a new instance based on validated serializer data:
        instance = serializer.save()

        # Create change log notification:
        self._create_notification(
            action=ActionTypeChoices.CREATE,
            log_changes=self.log_changes,
            serializer=serializer,
            user=request.user,
            instance=instance,
        )

        # Return (201 HTTP - Created) response:
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )
    
    def create(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:
        """
        Create a new model instance.
        """

        try:
            # Try to create a new instance:
            return self._call_create(
                request=request,
                *args,
                **kwargs,
            )
        
        # Return (400 HTTP - Bad Request) response:
        except ValidationError as exception:
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
