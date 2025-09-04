# AlpenWegs import:
from alpenwegs.ashared.api.schemas.exceptions_schemas import TokenAuthenticationAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import PermissionAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import ValidationAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import NotContentAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import ProtectedAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import NotFoundAPIExceptionSchema

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
                description=f'Retrieve {object_repr} objects',
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description=f'{object_repr} token authentication error'
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
                description=f'{object_repr} token authentication error'
            ),
            403: OpenApiResponse(
                PermissionAPIExceptionSchema,
                description=f'{object_repr} forbidden error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description=f'{object_repr} not found error'
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
                description=f'{object_repr} data validation error'
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description=f'{object_repr} token authentication error'
            ),
            403: OpenApiResponse(
                PermissionAPIExceptionSchema,
                description=f'{object_repr} forbidden error'
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
            200: OpenApiResponse(
                default_schema,
                description=f'Updated and retrieve {object_repr} object',
            ),
            400: OpenApiResponse(
                ValidationAPIExceptionSchema,
                description=f'{object_repr} data validation error'
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description=f'{object_repr} token authentication error'
            ),
            403: OpenApiResponse(
                PermissionAPIExceptionSchema,
                description=f'{object_repr} forbidden error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description=f'{object_repr} not found error'
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
            200: OpenApiResponse(
                default_schema,
                description=f'Updated and retrieve {object_repr} object',
            ),
            400: OpenApiResponse(
                ValidationAPIExceptionSchema,
                description=f'{object_repr} data validation error'
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description=f'{object_repr} token authentication error'
            ),
            403: OpenApiResponse(
                PermissionAPIExceptionSchema,
                description=f'{object_repr} forbidden error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description=f'{object_repr} not found error'
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
            204: OpenApiResponse(
                NotContentAPIExceptionSchema,
                description=f'{object_repr} no content response',
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description=f'{object_repr} token authentication error'
            ),
            403: OpenApiResponse(
                PermissionAPIExceptionSchema,
                description=f'{object_repr} forbidden error'
            ),
            404: OpenApiResponse(
                NotFoundAPIExceptionSchema,
                description=f'{object_repr} not found error'
            ),
            409: OpenApiResponse(
                ProtectedAPIExceptionSchema,
                description=f'{object_repr} conflict error'
            ),
        },
        tags=[f'{application_repr} - {object_repr}'],
    )
