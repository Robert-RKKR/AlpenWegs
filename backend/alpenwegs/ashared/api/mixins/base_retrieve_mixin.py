# AlpenWegs import:
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Rest framework import:
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status


class BaseRetrieveModelMixin(BaseMixin, RetrieveModelMixin):
    """
    Mixin class to retrieve a model instance.
    """
    
    def _call_retrieve(self):

        # Collect instance:
        instance = self.get_object()
        # Collect serializer:
        serializer = self.get_serializer(instance)
        # Return serializer data:
        return serializer.data

    def retrieve(self, request, *args, **kwargs):

        # Collect and return retrieve response:
        return Response(
            data=self._call_retrieve(),
            status=status.HTTP_200_OK
        )
