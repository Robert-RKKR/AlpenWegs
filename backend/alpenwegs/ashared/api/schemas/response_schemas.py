# Rest framework import:
from rest_framework import serializers


class BaseAPIResponseSchema(serializers.Serializer):
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
    page_error = None


class StandardAPIExceptionSchema(
    BaseAPIResponseSchema,
):
    """
    API schema for Permission exception.
    """

    pass
