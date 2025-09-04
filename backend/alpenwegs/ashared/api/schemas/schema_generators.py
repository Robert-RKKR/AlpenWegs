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
    optional_tag: str = None,
):

    # Create a dedicated schema for list responses:
    list_schema = extend_schema(
        # Define possible API responses:
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

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        list_schema.tags.append(optional_tag)

    # Return extended schema for list view:
    return list_schema

# Base retrieval schema generator
def schema_retrieve(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):

    # Create a dedicated schema for retrieval responses:
    retrieval_schema = extend_schema(
        # Define possible API responses:
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

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        retrieval_schema.tags.append(optional_tag)

    # Return extended schema for retrieval view:
    return retrieval_schema


# Base create schema generator
def schema_create(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):

    # Create a dedicated schema for create responses:
    create_schema = extend_schema(
        # Define possible API responses:
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

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        create_schema.tags.append(optional_tag)

    # Return extended schema for create view:
    return create_schema


# Base update schema generator
def schema_update(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):

    # Create a dedicated schema for update responses:
    update_schema = extend_schema(
        # Define possible API responses:
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

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        update_schema.tags.append(optional_tag)

    # Return extended schema for update view:
    return update_schema


# Base partial update schema generator
def schema_partial_update(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):

    # Create a dedicated schema for partial update responses:
    partial_update_schema = extend_schema(
        # Define possible API responses:
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

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        partial_update_schema.tags.append(optional_tag)

    # Return extended schema for partial update view:
    return partial_update_schema


# Base destroy schema generator
def schema_destroy(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):

    # Create a dedicated schema for destroy responses:
    destroy_schema = extend_schema(
        # Define possible API responses:
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

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        destroy_schema.tags.append(optional_tag)

    # Return extended schema for destroy view:
    return destroy_schema
