# AlpenWegs import:
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# Rest framework import:
from django.core.exceptions import FieldDoesNotExist
from rest_framework.mixins import ListModelMixin
from rest_framework.exceptions import ParseError
from rest_framework.decorators import action
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

    def _collect_queryset(self,
        admin: bool = False,
    ):
        """
        Default queryset restriction:
        - If model has `creator` field → restrict to objects created by the user.
        - Otherwise → return all objects.
        """

        # Check if user is admin:
        if admin:
            # Return all objects:
            return self.query_model.objects.all(
                ).order_by(
                    self.query_ordering
                )
        
        else:

            try:
                # Check if model has creator field:
                self.query_model._meta.get_field('creator')
                
                # Filter only objects created by the requesting user:
                return self.query_model.objects.filter(
                    creator=self.request.user,
                ).order_by(
                    self.query_ordering
                )
            
            except FieldDoesNotExist:
                # Return all objects:
                return self.query_model.objects.all(
                    ).order_by(
                        self.query_ordering
                    )

    def _call_list(self,
        admin: bool,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        # Collect all instances:
        queryset = self.filter_queryset(self._collect_queryset(admin))
        
        # Prepare page view with pagination:
        page = self.paginate_queryset(queryset)
        if page is not None:
            # if page has been received, serializer it:
            serializer = self.get_serializer(page, many=True)
            paginated = self.get_paginated_response(serializer.data)
            return paginated
        
        # Prepare page view without pagination:
        serializer = self.get_serializer(queryset, many=True)

        # Return (200 HTTP - Ok) response:
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
                False,
                request=request,
                *args,
                **kwargs,
            )

        # Unexpected exception handling !TEMPORARY:
        except Exception as exception:
            # Test exceptions:
            print(f'Type of list exception: {type(exception)}')
            
            # Raise not found error:
            raise ParseError(
                'An error occurred during the GET List API call.',
            )

    @action(detail=False, methods=['get'], url_path='admin')
    def admin(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        try:
            # Try to collect all instances:
            return self._call_list(
                True,
                request=request,
                *args,
                **kwargs,
            )

        # Unexpected exception handling !TEMPORARY:
        except Exception as exception:
            # Test exceptions:
            print(f'Type of list exception: {type(exception)}')
            
            # Raise not found error:
            raise ParseError(
                'An error occurred during the GET List API call.',
            )
