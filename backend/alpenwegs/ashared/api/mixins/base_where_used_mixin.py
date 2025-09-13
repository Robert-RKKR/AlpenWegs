# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import NotFoundAPIException
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Rest framework import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http.response import Http404
from rest_framework import status


class BaseWhereUsedModelMixin(
    BaseMixin,
    RetrieveModelMixin,
):
    """
    Mixin class to where_used a model instance.
    """
    
    def _call_where_used(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        # Collect instance:
        instance = self.get_object()
        # Collect serializer:
        serializer = self._get_serializer(   
            instance,
            serializer_name='where_used',
        )

        # Return (200 HTTP - Ok) response:
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=['get'], url_path='where-used')
    def where_used(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        try:
            # Try to collect a single instance:
            return self._call_where_used(
                request=request,
                *args,
                **kwargs,
            )
        
        # Return (404 HTTP - Not Found) response:
        except Http404 as exception:
            # Define error details list:
            error_details = {
                'error_field': kwargs,
                'error_message': 'Item with provided PK value does not exist.',
                'error_code': 'item_not_found',
            }
            
            # Raise validation API exception with collected details:
            raise NotFoundAPIException(
                error_details=error_details,
            )
