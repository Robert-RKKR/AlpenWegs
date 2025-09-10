# AlpenWegs import:
from alpenwegs.ashared.api.schemas.exceptions_schemas import TokenAuthenticationAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import PermissionAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import ValidationAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import NotContentAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import ProtectedAPIExceptionSchema
from alpenwegs.ashared.api.schemas.exceptions_schemas import NotFoundAPIExceptionSchema
from alpenwegs.ashared.api.schemas.response_schemas import StandardAPIExceptionSchema

# Drf spectacular import:
from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework import serializers

def build_paginated_list_schema(data_schema):
    """
    Custom schema matching your actual paginated response format.
    """
    class PaginatedListSchema(serializers.Serializer):
        page_status = serializers.BooleanField()
        page_results = data_schema(many=True)
        page_objects = serializers.IntegerField()
        page_count = serializers.IntegerField()
        page_links = serializers.DictField(
            child=serializers.CharField(allow_null=True)
        )
        page_error = serializers.JSONField(allow_null=True, required=False)

    PaginatedListSchema.__name__ = f"{data_schema.__name__}PaginatedListResponse"
    return PaginatedListSchema


def build_list_schema(data_schema):
    """
    Wrapper for list responses (paginated or not).
    """
    class ListSchema(serializers.Serializer):
        page_status = serializers.BooleanField()
        page_results = data_schema(many=True)
        page_error = serializers.JSONField(allow_null=True, required=False)

    suffix = "ListResponse"
    ListSchema.__name__ = f"{data_schema.__name__}{suffix}"
    return ListSchema


def build_retrieve_schema(data_schema):
    """
    Wrapper for single object responses.
    """
    class RetrieveSchema(serializers.Serializer):
        page_status = serializers.BooleanField()
        page_results = data_schema()
        page_error = serializers.JSONField(allow_null=True, required=False)

    RetrieveSchema.__name__ = f"{data_schema.__name__}RetrieveResponse"
    return RetrieveSchema


# Base list schema generator:
def schema_list(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):
    """
    Schema generator for standard list views.

    - Returns only objects created by the requesting user
      OR objects that are publicly visible (`is_public=True`).
    - Intended for standard users to retrieve their own data
      and public entries of the model.
    """

    # Generate paginated list schema based on model serializer:
    response_schema = build_paginated_list_schema(default_schema)

    # Create a dedicated schema for list responses:
    list_schema = extend_schema(
        # Define possible API responses:
        responses={
            200: OpenApiResponse(
                response_schema,
                description=f'Retrieve {object_repr} objects',
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description=f'{object_repr} token authentication error'
            ),
        },

        # Add description and summary to schema:
        description=f'Retrieve a filtered list of {object_repr} objects '
            'created by the requesting user or available for public view. '
            'Some user groups may be permitted to view all objects '
            'regardless of ownership or public status, but to receive all '
            'objects they need to use the admin view.',
        summary=f'List all user created or publicly available {object_repr} objects.',

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        list_schema.tags.append(optional_tag)

    # Return extended schema for list view:
    return list_schema


# Base admin schema generator:
def schema_admin(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):
    """
    Schema generator for admin list views.

    - Returns **all** objects of the given model in the system,
      regardless of ownership or public status.
    - Restricted to administrative users only.
    """

    # Generate paginated list schema based on model serializer:
    response_schema = build_paginated_list_schema(default_schema)

    # Create a dedicated schema for admin responses:
    admin_schema = extend_schema(
        # Define possible API responses:
        responses={
            200: OpenApiResponse(
                response_schema,
                description=f'Retrieve {object_repr} objects',
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description=f'{object_repr} token authentication error'
            ),
        },

        # Add description and summary to schema:
        description=f'Admin-only endpoint that retrieves all {object_repr} '
            'objects in the AlpenWeg application. Only users that belong to '
            'the Admin group have access to this view.',
        summary=f'List all {object_repr} objects (Admin user only).',

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        admin_schema.tags.append(optional_tag)

    # Return extended schema for admin view:
    return admin_schema


# Base representation schema generator:
def schema_representation(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):
    """
    Schema generator for representation list views.

    - Returns **all** objects of the given model in the system,
      regardless of ownership or public status, without pagination.
    - Available for all users.
    """

    # Generate non-paginated list schema based on model serializer:
    response_schema = build_list_schema(default_schema)

    # Create a dedicated schema for representation responses:
    representation_schema = extend_schema(
        # Define possible API responses:
        responses={
            200: OpenApiResponse(
                response_schema,
                description=f'Retrieve {object_repr} objects',
            ),
            401: OpenApiResponse(
                TokenAuthenticationAPIExceptionSchema,
                description=f'{object_repr} token authentication error'
            ),
        },

        # Add description and summary to schema:
        description=f'Fully available endpoint that retrieves all {object_repr} '
            'objects in the AlpenWeg application.',
        summary=f'Representative list all {object_repr} objects.',

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        representation_schema.tags.append(optional_tag)

    # Return extended schema for representation view:
    return representation_schema

# Base retrieval schema generator:
def schema_retrieve(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):
    """
    Schema generator for retrieving a single object.

    - Returns one {object_repr} object if the user has permission.
    - Ensures object visibility and ownership are respected.
    """

    # Generate retrieval schema based on model serializer:
    response_schema = build_retrieve_schema(default_schema)

    # Create a dedicated schema for retrieval responses:
    retrieval_schema = extend_schema(
        # Define possible API responses:
        responses={
            200: OpenApiResponse(
                response_schema,
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

        # Add description and summary to schema:
        description='Retrieve detailed information about a specific '
            f'{object_repr} object. The object must be created by the '
            'requesting user or be available as public. Some user groups '
            'may be permitted to view all objects regardless of ownership '
            'or public status of given object.',
        summary=f'Retrieve single {object_repr} object.',

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        retrieval_schema.tags.append(optional_tag)

    # Return extended schema for retrieval view:
    return retrieval_schema


# Base create schema generator:
def schema_create(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):
    """
    Schema generator for creating a new object.

    - Allows users to submit data to create a new {object_repr}.
    - Returns the created object upon success.
    """

    # Generate create schema based on model serializer:
    response_schema = build_retrieve_schema(default_schema)

    # Create a dedicated schema for create responses:
    create_schema = extend_schema(
        # Define possible API responses:
        responses={
            201: OpenApiResponse(
                response_schema,
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

        # Add description and summary to schema:
        description=f'Create a new {object_repr} object based on the '
            'provided data. Allowed only for users that belongs to '
            'groups with sufficient privileges to perform object creation.',
        summary=f'Create new {object_repr} object.',

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        create_schema.tags.append(optional_tag)

    # Return extended schema for create view:
    return create_schema


# Base update schema generator:
def schema_update(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):
    """
    Schema generator for full updates.

    - Allows replacing all fields of an existing {object_repr}.
    - Returns the updated object.
    """

    # Generate update schema based on model serializer:
    response_schema = build_retrieve_schema(default_schema)

    # Create a dedicated schema for update responses:
    update_schema = extend_schema(
        # Define possible API responses:
        responses={
            200: OpenApiResponse(
                response_schema,
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

        # Add description and summary to schema:
        description=f'Perform a full update on an existing {object_repr}. '
            'object. Some user groups can update only objects they created, '
            'while others may be permitted to update all objects, regardless '
            'of ownership or public status of given object.',
        summary=f'Update existing {object_repr} object.',

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        update_schema.tags.append(optional_tag)

    # Return extended schema for update view:
    return update_schema


# Base partial update schema generator:
def schema_partial_update(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):
    """
    Schema generator for partial updates.

    - Allows updating specific fields of an existing {object_repr}.
    - Returns the updated object.
    """

    # Generate partial update schema based on model serializer:
    response_schema = build_retrieve_schema(default_schema)

    # Create a dedicated schema for partial update responses:
    partial_update_schema = extend_schema(
        # Define possible API responses:
        responses={
            200: OpenApiResponse(
                response_schema,
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

        # Add description and summary to schema:
        description=f'Perform a partial update on an existing {object_repr}. '
            'object. Some user groups can update only objects they created, '
            'while others may be permitted to update all objects, regardless '
            'of ownership or public status of given object.',
        summary=f'Partially update existing {object_repr} object.',

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        partial_update_schema.tags.append(optional_tag)

    # Return extended schema for partial update view:
    return partial_update_schema


# Base destroy schema generator:
def schema_destroy(
    default_schema: serializers.Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
):
    """
    Schema generator for deletion.

    - Deletes a {object_repr} object if permitted.
    - Returns no content upon success.
    """

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

        # Add description and summary to schema:
        description=f'Delete a specific {object_repr} object if permitted. '
            'Some user groups can delete only objects they created, while '
            'others may be permitted to delete all objects, regardless '
            'of ownership or public status of given object. Returns no '
            'content upon success.',
        summary=f'Delete {object_repr} object.',

        # Add tag to schema:
        tags=[f'{application_repr} - {object_repr}'],
    )

    # Add additional tag if provided:
    if optional_tag is not None:
        # Add tag to existing list:
        destroy_schema.tags.append(optional_tag)

    # Return extended schema for destroy view:
    return destroy_schema
