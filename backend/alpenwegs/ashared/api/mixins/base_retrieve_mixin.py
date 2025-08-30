# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import NotFoundAPIException
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Rest framework import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status


class BaseRetrieveModelMixin(
    BaseMixin,
    RetrieveModelMixin,
):
    """
    Mixin class to retrieve a model instance.
    """
    
    def _call_retrieve(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        # Collect instance:
        instance = self.get_object()
        # Collect serializer:
        serializer = self.get_serializer(instance)

        # Return HTTP response 200 object was created:
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def retrieve(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        try:
            # Try to create a new instance:
            return self._call_retrieve(
                request=request,
                *args,
                **kwargs,
            )
        
        except Http404:
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
