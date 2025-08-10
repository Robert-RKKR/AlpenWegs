# Rest framework import:
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status

# AlpenWegs import:
from alpenwegs.ashared.constants.notification import ApplicationChoices
from alpenwegs.ashared.api.mixins.base_mixin import BaseMixin

# AlpenWegs application import:
from notification.ashared import Notification
from notification.ashared import Logger

# Django import:
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.contrib import admin

# Python import:
import copy
import uuid

# Init API notification:
notification = Notification(
    'API', channel_name='objects_notifications')
task_id = str(uuid.uuid4())
logger = Logger(ApplicationChoices.API, task_id)


class BaseListModelMixin(BaseMixin, ListModelMixin):
    """
    List a queryset.
    """

    def _call_list(self, request, *args, **kwargs):

        # Collect all instances:
        queryset = self.filter_queryset(self.get_queryset())
        # Prepare page view with pagination:
        page = self.paginate_queryset(queryset)
        if page is not None:
            # if page has been received, serializer it:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # Serializer respond:
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):

        try: # Try to make a nwe API GET - List call:
            response = self._call_list(request, *args, **kwargs)
        except Exception as exception: # Define error code:
            error_code = status.HTTP_400_BAD_REQUEST
            # Create a new log notification:
            self._log_api_call(request, True, error_code)
            # Return HTTP response 400 - Bad request:
            return self._return_api_error(
                error_code, exception.__class__.__name__,
                str(exception))
        else: # Create a new log notification:
            self._log_api_call(request)
            # Return collected response:
            return response
