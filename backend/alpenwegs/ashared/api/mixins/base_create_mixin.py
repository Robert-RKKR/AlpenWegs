# Rest framework import:
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.exceptions import ParseError
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

        # Collect serializer:
        serializer = self.get_serializer(data=request.data)
        
        try: # try to validate serializer:
            print(f'request data: {request.data} user: {request.user}')
            serializer.is_valid(raise_exception=True)
        
        except ValidationError as exception:
            print(f'Validation error: {exception}')
            # Raise not found error:
            raise ParseError(f'The provided data are incorrect. {self.format_validation_error(exception)}')
        
        except Exception as exception:
            # Raise not found error:
            raise ValidationError(f'An error occurred during data validation. {str(exception)}')
        
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
