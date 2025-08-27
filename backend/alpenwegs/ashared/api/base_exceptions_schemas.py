# Rest framework import:
from rest_framework import serializers
from rest_framework import status



class BaseAPIExceptionSchema(serializers.Serializer):
    """
    Base schema for API error responses.
    """

    class BaseSubSchema(serializers.Serializer):
        """
        Single error detail for page_error.
        """

        error_message = serializers.CharField()
        error_status = serializers.IntegerField()
        error_code = serializers.CharField()
        error_details = serializers.BooleanField()

    page_status = serializers.BooleanField()
    page_data = serializers.JSONField()
    page_error = serializers.DictField(
        child=serializers.ListSerializer(
            child=BaseSubSchema()
        ),
    )


class TokenAuthenticationAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    Raised when validation fails (e.g. serializer.is_valid).
    """

    class TokenAuthenticationSubSchema(
        serializers.Serializer
    ):
        """
        Single error detail for page_error.
        """

        token_class = serializers.CharField()
        token_type = serializers.CharField()
        message = serializers.CharField()

    # override page error sub schema:
    page_error = serializers.DictField(
        child=serializers.ListSerializer(
            child=TokenAuthenticationSubSchema()
        ),
    )


# class PermissionAPIExceptionSchema(
#     BaseAPIExceptionSchema,
# ):
#     """
#     Raised when permission is denied.
#     """

#     status_code = status.HTTP_403_FORBIDDEN
#     default_message = (
#         'You do not have the required permissions to perform this action. '
#         'If you believe this is a mistake, please contact an administrator.'
#     )
#     default_code = 'permission_denied'
#     default_detail = []


class ValidationAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    Raised when object is not found.
    """

    pass


class NotFoundAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    Raised when object is not found.
    """

    pass


# class ServerAPIExceptionSchema(
#     BaseAPIExceptionSchema,
# ):
#     """
#     Raised for unexpected server errors.
#     """

#     status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#     default_message = (
#         'An internal server error occurred while processing your request. '
#         'Our team has been notified, and we are working to resolve the issue.'
#     )
#     default_code = 'server_error'
#     default_detail = []
