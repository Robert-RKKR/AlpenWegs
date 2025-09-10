# AlpenWegs application import:
from notifications.api.serializers.change_log_serializer import ChangeLogRepresentationSerializer
from notifications.api.serializers.change_log_serializer import ChangeLogWithoutAfterSerializer
from notifications.api.serializers.change_log_serializer import ChangeLogDetailedSerializer
from notifications.api.serializers.change_log_serializer import ChangeLogRelationSerializer
from notifications.api.filters.change_log_filter import ChangeLogFilter
from notifications.models.change_log_model import ChangeLogModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_representation
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_list
from alpenwegs.ashared.api.base_model_viewset import ReadOnlyViewSet

# API import:
from drf_spectacular.utils import extend_schema_view
from rest_framework.response import Response
from rest_framework.decorators import action


# ChangeLog Model api view class:
@extend_schema_view(
    representation=schema_representation(ChangeLogDetailedSerializer, 'Notifications', 'Change Log'),
    compare_changes=schema_retrieve(ChangeLogDetailedSerializer, 'Notifications', 'Change Log'),
    retrieve=schema_retrieve(ChangeLogDetailedSerializer, 'Notifications', 'Change Log'),
    admin=schema_list(ChangeLogDetailedSerializer, 'Notifications', 'Change Log'),
    list=schema_list(ChangeLogDetailedSerializer, 'Notifications', 'Change Log'),
)
class ChangeLogView(
    ReadOnlyViewSet,
):
    """
    Change Log Read and write view.
    """

    # Queryset for the view (Legacy, required by DRF):
    queryset = ChangeLogModel.objects.all()

    # Model and query ordering used for the view:
    query_model = ChangeLogModel
    query_ordering = '-created'

    # Serializer class (Legacy, required by DRF):
    serializer_class = ChangeLogDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = ChangeLogRepresentationSerializer
    detailed_serializer_class = ChangeLogDetailedSerializer
    relation_serializer_class = ChangeLogRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = ChangeLogFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'

    @action(detail=True, methods=['get'], url_path='compare-changes')
    def compare_changes(self, request, pk=None):
        """
        Custom method to retrieve current change log and append the previous
        change log's 'after' value as part of the current change's response.
        """

        # Get the current change object:
        current_change = self.get_object()
        
        # Collect current change related AlpenWegs object:
        current_change_app_name = current_change.app_name
        current_change_model_name = current_change.model_name
        current_change_object_id = current_change.object_id
        
        # Get the previous change object for the same object:
        previous_change = ChangeLogModel.objects.filter(
            app_name=current_change_app_name,
            model_name=current_change_model_name,
            object_id=current_change_object_id,
            timestamp__lt=current_change.timestamp
        ).order_by('-timestamp').first()
        
        # Build the response data:
        data = {
            'change_object': ChangeLogWithoutAfterSerializer(
                current_change, context={'request': request}).data,
            'current_change': current_change.after,
            'previous_change': previous_change.after if previous_change else None
        }
        
        # Return collected data:
        return Response(data)
