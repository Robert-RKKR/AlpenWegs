# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_partial_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_representation
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_destroy
from alpenwegs.ashared.api.schemas.schema_generators import schema_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_create
from alpenwegs.ashared.api.schemas.schema_generators import schema_admin
from alpenwegs.ashared.api.schemas.schema_generators import schema_list

# Drf spectacular import:
from rest_framework.serializers import Serializer

# Read Write Schema Generator:
def red_write_schema(
    representation_schema: Serializer,
    detailed_schema: Serializer,
    relation_schema: Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
    where_used_schema: Serializer = None,
    **additional_schemas,
) -> tuple:

    # Generate and return Model schema:
    generated_schema = {
        'representation': schema_representation(
            response_schema=representation_schema,
            application_repr=application_repr,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'partial_update': schema_partial_update(
            application_repr=application_repr,
            response_schema=detailed_schema,
            request_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'retrieve': schema_retrieve(
            application_repr=application_repr,
            response_schema=detailed_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'destroy': schema_destroy(
            application_repr=application_repr,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'update': schema_update(
            application_repr=application_repr,
            response_schema=detailed_schema,
            request_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'create': schema_create(
            application_repr=application_repr,
            response_schema=detailed_schema,
            request_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'admin': schema_admin(
            application_repr=application_repr,
            response_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'list': schema_list(
            application_repr=application_repr,
            response_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
    }

    # Add where used schema if provided:
    if where_used_schema:
        generated_schema['where_used'] = schema_retrieve(
            application_repr=application_repr,
            response_schema=where_used_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        )

    # Add additional schemas if provided:
    if additional_schemas:
        # Iterate over additional schemas:
        for key, schema in additional_schemas.items():
            # Add additional schema to generated schema:
            generated_schema[key] = schema

    # Return generated schema:
    return generated_schema

# Read Only Schema Generator:
def red_only_schema(
    representation_schema: Serializer,
    detailed_schema: Serializer,
    relation_schema: Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
) -> tuple:

    # Generate and return Model schema:
    return {
        'representation': schema_representation(
            response_schema=representation_schema,
            application_repr=application_repr,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'retrieve': schema_retrieve(
            application_repr=application_repr,
            response_schema=detailed_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'admin': schema_admin(
            application_repr=application_repr,
            response_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'list': schema_list(
            application_repr=application_repr,
            response_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
    }

# Read Delete Schema Generator:
def red_delete_schema(
    representation_schema: Serializer,
    detailed_schema: Serializer,
    relation_schema: Serializer,
    application_repr: str,
    object_repr: str,
    optional_tag: str = None,
) -> tuple:

    # Generate and return Model schema:
    return {
        'representation': schema_representation(
            response_schema=representation_schema,
            application_repr=application_repr,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'retrieve': schema_retrieve(
            application_repr=application_repr,
            response_schema=detailed_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'destroy': schema_destroy(
            application_repr=application_repr,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'admin': schema_admin(
            application_repr=application_repr,
            response_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
        'list': schema_list(
            application_repr=application_repr,
            response_schema=relation_schema,
            optional_tag=optional_tag,
            object_repr=object_repr,
        ),
    }

