# Drf spectacular import:
from rest_framework import serializers

def build_paginated_list_schema(
    default_schema: serializers.Serializer,
    schema_name: str,
):
    """
    Custom schema wrapper for paginated list responses.

    This function creates a new serializer class that wraps
    the provided default schema in a paginated response format.
    To keep base schema response style for AlpenWegs API.
    """

    class PaginatedListSchema(
        serializers.Serializer,
    ):
        """
        Base schema for paginated list responses.
        """

        page_status = serializers.BooleanField()
        page_results = default_schema(many=True)
        page_objects = serializers.IntegerField()
        page_count = serializers.IntegerField()
        page_links = serializers.DictField(
            child=serializers.CharField(allow_null=True)
        )
        page_error = serializers.JSONField(
            allow_null=True,
            required=False,
        )

    # Create a unique name for the schema class:
    unique_schema_name = f'{default_schema.__name__}{schema_name}'
    # Add created name to schema class:
    PaginatedListSchema.__name__ = f'{unique_schema_name}SchemaResponse'
    # Return created schema:
    return PaginatedListSchema

def build_list_schema(
    default_schema: serializers.Serializer,
    schema_name: str,
):
    """
    Custom schema wrapper for not paginated list responses.

    This function creates a new serializer class that wraps
    the provided default schema in a paginated response format.
    To keep base schema response style for AlpenWegs API.
    """

    class ListSchema(
        serializers.Serializer,
    ):
        """
        Base schema for not paginated list responses.
        """

        page_status = serializers.BooleanField()
        page_results = default_schema(many=True)
        page_error = serializers.JSONField(
            allow_null=True,
            required=False,
        )

    # Create a unique name for the schema class:
    unique_schema_name = f'{default_schema.__name__}{schema_name}'
    # Add created name to schema class:
    ListSchema.__name__ = f'{unique_schema_name}SchemaResponse'
    # Return created schema:
    return ListSchema

def build_retrieve_schema(
    default_schema: serializers.Serializer,
    schema_name: str,
):
    """
    Custom schema wrapper for retrieve responses.

    This function creates a new serializer class that wraps
    the provided default schema in a paginated response format.
    To keep base schema response style for AlpenWegs API.
    """

    class RetrieveSchema(
        serializers.Serializer,
    ):
        """
        Base schema for retrieve responses.
        """

        page_status = serializers.BooleanField()
        page_results = default_schema()
        page_error = serializers.JSONField(
            allow_null=True,
            required=False,
        )

    # Create a unique name for the schema class:
    unique_schema_name = f'{default_schema.__name__}{schema_name}'
    # Add created name to schema class:
    RetrieveSchema.__name__ = f'{unique_schema_name}SchemaResponse'
    # Return created schema:
    return RetrieveSchema
