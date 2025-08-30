# AlpenWegs import:
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Rest framework import:
from rest_framework.mixins import ListModelMixin
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

# Django import:
from django.db import models


class BaseListModelMixin(
    BaseMixin,
    ListModelMixin,
):
    """
    Base model mixin for listing a queryset.
    """

    # Define custom list values:
    allow_list = False

    def _call_list(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        # Collect all instances:
        queryset = self.filter_queryset(self.get_queryset())
        
        # Prepare page view with pagination:
        page = self.paginate_queryset(queryset)
        if page is not None:
            # if page has been received, serializer it:
            serializer = self.get_serializer(page, many=True)
            paginated = self.get_paginated_response(serializer.data)
            return paginated.data
        
        # Prepare page view without pagination:
        serializer = self.get_serializer(queryset, many=True)
        return serializer.data

    def list(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        try:
            # Run a new API GET List call:
            response = self._call_list(
                request=request,
                *args,
                **kwargs,
            )

        except Exception:
            # Raise not found error:
            raise ParseError(
                'An error occurred during the GET List API call.',
            )
        
        else:
            # Return collected response:
            return Response(response)
