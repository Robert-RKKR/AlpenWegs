# Rest framework import:
from rest_framework.exceptions import APIException
from rest_framework import status


# Base Application API Exception:
class BaseAPIException(
    APIException,
):
    """
    Custom base exception for AlpenWegs API.
    All custom errors should inherit from this.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_message = 'An error occurred.'
    default_code = 'api_error'
    default_detail = []

    def __init__(self,
        status_code: status = None,
        error_message: str = None,
        error_details: str = None,
        error_code: str = None,
    ):

        if status_code is not None:
            self.status_code = status_code
        if error_code is not None:
            self.default_code = error_code

        self.detail = {
            'detail': error_message or self.default_message,
            'messages': error_details or self.default_code,
            'code': error_code or self.default_code,
        }


class ValidationAPIException(
    BaseAPIException,
):
    """
    Raised when validation fails (e.g. serializer.is_valid).
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_message = (
        'The data you provided is invalid. Please check each field for errors '
        'and correct them before trying again.'
    )
    default_code = 'validation_error'
    default_detail = []


class PermissionAPIException(
    BaseAPIException,
):
    """
    Raised when permission is denied.
    """

    status_code = status.HTTP_403_FORBIDDEN
    default_message = (
        'You do not have the required permissions to perform this action. '
        'If you believe this is a mistake, please contact an administrator.'
    )
    default_code = 'permission_denied'
    default_detail = []


class NotFoundAPIException(
    BaseAPIException,
):
    """
    Raised when object is not found.
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_message = (
        'The requested resource could not be found. It may have been '
        'removed or are temporarily unavailable.'
    )
    default_code = 'not_found'
    default_detail = []


class ServerAPIException(
    BaseAPIException,
):
    """
    Raised for unexpected server errors.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_message = (
        'An internal server error occurred while processing your request. '
        'Our team has been notified, and we are working to resolve the issue.'
    )
    default_code = 'server_error'
    default_detail = []
