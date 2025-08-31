# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions_schemas import TokenAuthenticationAPIExceptionSchema
from alpenwegs.ashared.api.base_exceptions_schemas import ValidationAPIExceptionSchema
from alpenwegs.ashared.api.base_exceptions_schemas import ProtectedAPIExceptionSchema
from alpenwegs.ashared.api.base_exceptions_schemas import NotFoundAPIExceptionSchema

# Drf spectacular import:
from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework import serializers


# Base list schema generator
def schema_list(
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
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description='Token authentication error'
            ),
        },
        tags=[f'{application_repr} - {object_repr}'],
    )


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
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description='Token authentication error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description='Object not found error'
            ),
        },
        tags=[f'{application_repr} - {object_repr}'],
    )


# Base create schema generator
def schema_create(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
):
    
    return extend_schema(
        responses={
            201: OpenApiResponse(
                default_schema,
                description=f'Retrieve {object_repr} object',
            ),
            400: OpenApiResponse(
                ValidationAPIExceptionSchema,
                description='Data validation error'
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description='Token authentication error'
            ),
        },
        tags=[f'{application_repr} - {object_repr}'],
    )


# Base update schema generator
def schema_update(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
):
    
    return extend_schema(
        responses={
            201: OpenApiResponse(
                default_schema,
                description=f'Retrieve {object_repr} object',
            ),
            400: OpenApiResponse(
                ValidationAPIExceptionSchema,
                description='Data validation error'
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description='Token authentication error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description='Object not found error'
            ),
        },
        tags=[f'{application_repr} - {object_repr}'],
    )


# Base partial update schema generator
def schema_partial_update(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
):
    
    return extend_schema(
        responses={
            201: OpenApiResponse(
                default_schema,
                description=f'Retrieve {object_repr} object',
            ),
            400: OpenApiResponse(
                ValidationAPIExceptionSchema,
                description='Data validation error'
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description='Token authentication error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description='Object not found error'
            ),
        },
        tags=[f'{application_repr} - {object_repr}'],
    )


# Base destroy schema generator
def schema_destroy(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
):
    
    return extend_schema(
        responses={
            201: OpenApiResponse(
                default_schema,
                description=f'Retrieve {object_repr} object',
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description='Token authentication error'
            ),
            403: OpenApiResponse(
                ProtectedAPIExceptionSchema,
                description='Object protected error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description='Object not found error'
            ),
        },
        tags=[f'{application_repr} - {object_repr}'],
    )
