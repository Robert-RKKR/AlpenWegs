# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions_schemas import TokenAuthenticationAPIExceptionSchema
from alpenwegs.ashared.api.base_exceptions_schemas import ValidationAPIExceptionSchema
from alpenwegs.ashared.api.base_exceptions_schemas import NotFoundAPIExceptionSchema

# Drf spectacular import:
from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework import serializers


# Base retrieval schema generator
def schema_retrieve(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
):
    
    return extend_schema(
        responses={
            200: OpenApiResponse(
                default_schema,
                description=f'Retrieve {object_repr} object',
            ),
            400: OpenApiResponse(
                ValidationAPIExceptionSchema,
                description='Validation error'
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description='Validation error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description='Not found'
            ),
        },
        tags=[f'{application_repr} - {object_repr}'],
    )

