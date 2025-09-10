# AlpenWegs application import:
from notifications.api.serializers.notification_serializer import NotificationRepresentationSerializer
from notifications.api.serializers.notification_serializer import NotificationDetailedSerializer
from notifications.api.serializers.notification_serializer import NotificationRelationSerializer
from notifications.api.filters.notification_filter import NotificationFilter
from notifications.models.notification_model import NotificationModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_representation
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_destroy
from alpenwegs.ashared.api.schemas.schema_generators import schema_list
from alpenwegs.ashared.api.base_model_viewset import ReadDeleteViewSet

# Drf spectacular import:
from drf_spectacular.utils import extend_schema_view


# Notification Model api view class:
@extend_schema_view(
    representation=schema_representation(NotificationDetailedSerializer, 'Assets', 'File'),
    retrieve=schema_retrieve(NotificationDetailedSerializer, 'Notification', 'Notification'),
    destroy=schema_destroy(NotificationDetailedSerializer, 'Notification', 'Notification'),
    admin=schema_list(NotificationDetailedSerializer, 'Notification', 'Notification'),
    list=schema_list(NotificationDetailedSerializer, 'Notification', 'Notification'),
)
class NotificationView(
    ReadDeleteViewSet,
):
    """
    Notification Read and write view.
    """

    # Queryset for the view (Legacy, required by DRF):
    queryset = NotificationModel.objects.all()

    # Model and query ordering used for the view:
    query_model = NotificationModel
    query_ordering = '-created'

    # Serializer class (Legacy, required by DRF):
    serializer_class = NotificationDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = NotificationRepresentationSerializer
    detailed_serializer_class = NotificationDetailedSerializer
    relation_serializer_class = NotificationRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = NotificationFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
