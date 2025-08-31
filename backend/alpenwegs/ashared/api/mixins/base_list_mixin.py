# AlpenWegs import:
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Rest framework import:
from rest_framework.mixins import ListModelMixin
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import status


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

        # Return HTTP response 200 objects has been collected:
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def list(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        try:
            # Try to collect all instances:
            return self._call_list(
                request=request,
                *args,
                **kwargs,
            )

        except Exception as exception:
            # Test exceptions:
            print(f'Type of list exception: {type(exception)}')
            
            # Raise not found error:
            raise ParseError(
                'An error occurred during the GET List API call.',
            )