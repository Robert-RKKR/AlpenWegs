# Rest framework import:
from rest_framework import serializers


class BaseAPIExceptionSchema(serializers.Serializer):
    """
    Default general API schema for exceptions.
    """

    class BaseSubSchema(
        serializers.Serializer
    ):

        # Sub schema fields:
        error_message = serializers.CharField()
        error_status = serializers.IntegerField()
        error_code = serializers.CharField()
        error_details = serializers.BooleanField()

    # Main schema fields:
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
    API schema for Token Authentication exception.
    """

    class TokenAuthenticationSubSchema(
        serializers.Serializer
    ):

        # Sub schema fields:
        token_class = serializers.CharField()
        token_type = serializers.CharField()
        message = serializers.CharField()

    # Override page error sub schema:
    page_error = serializers.DictField(
        child=serializers.ListSerializer(
            child=TokenAuthenticationSubSchema()
        ),
    )


class PermissionAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    API schema for Permission exception.
    """

    pass


class ValidationAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    API schema for Validation exception.
    """

    pass


class NotFoundAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    API schema for Not Found exception.
    """

    pass


class NotContentAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    API schema for Not Content exception.
    """

    # Main schema fields:
    page_data = None
    page_error = None


class ServerAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    API schema for Server exception.
    """

    pass


class ProtectedAPIExceptionSchema(
    BaseAPIExceptionSchema,
):
    """
    API schema for Protected exception.
    """

    pass
