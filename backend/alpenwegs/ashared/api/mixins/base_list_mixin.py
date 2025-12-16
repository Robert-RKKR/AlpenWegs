# AlpenWegs import:
from alpenwegs.ashared.api.base_exceptions import PermissionAPIException
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# AlpenWegs application import:
from profiles.models.user_model import UserModel

# Rest framework import:
from django.core.exceptions import FieldDoesNotExist
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

    def _collect_queryset(self):
        """
        Default queryset restriction:
        - If model has `creator` field → restrict to objects created by the user.
        - Otherwise → return all objects.
        """

        # Check if user is authenticated:
        if not self.request.user.is_authenticated:
            
            try:
                # If model supports public visibility, return only public objects:
                self.query_model._meta.get_field('is_public')

                # Return only public objects:
                return self.query_model.objects.filter(
                    is_public=True
                ).order_by(
                    self.query_ordering
                )
            
            # If model has no public field:
            except FieldDoesNotExist:
                # Return empty queryset:
                return self.query_model.objects.none()

        # Check if request user is instance of UserModel:
        if isinstance(self.query_model, UserModel):
            # Filter only user that is requesting the data:
            return self.query_model.objects.filter(
                pk=self.request.user.pk,
            ).order_by(
                self.query_ordering
            )

        # If user is authenticated, and is not UserModel instance:
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
            # Define error details list:
            error_details = {
                'error_message': 'Model does not have a creator field.',
                'error_code': 'permission_denied',
            }

            # Raise validation API exception with collected details:
            raise PermissionAPIException(
                error_details=error_details,
            )

    def _call_list(self,
        request: Response,
        *args: list,
        **kwargs: dict,
    ) -> Response:

        # Collect all instances:
        queryset = self.filter_queryset(
            self._collect_queryset()
        )
        
        # Prepare page view with pagination:
        page = self.paginate_queryset(queryset)
        if page is not None:
            # If page has been received, serializer it:
            serializer = self._get_serializer(
                page,
                serializer_name='relation',
                many=True
            )
            # Prepare paginated response:
            paginated = self.get_paginated_response(
                serializer.data
            )
            # Return paginated response:
            return paginated
        
        # Prepare page view without pagination:
        serializer = self._get_serializer(
            queryset,
            serializer_name='relation',
            many=True,
        )

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


        # Try to collect all instances:
        return self._call_list(
            request=request,
            *args,
            **kwargs,
        )