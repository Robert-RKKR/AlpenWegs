# AlpenWegs application import:
from notifications.api.serializers.notification_serializer import NotificationSerializer
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from notifications.api.filters.notification_filter import NotificationFilter
from notifications.models.notification_model import NotificationModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_destroy
from alpenwegs.ashared.api.schemas.schema_generators import schema_list
from alpenwegs.ashared.api.base_model_viewset import ReadDeleteViewSet
from profiles.api.serializers.user_serializer import UserSerializer

# Drf spectacular import:
from drf_spectacular.utils import extend_schema_view
from drf_spectacular.utils import extend_schema


# Notification Model api view class:
@extend_schema_view(
    retrieve=schema_retrieve(UserSerializer, 'Notification', 'Notification'),
    destroy=schema_destroy(UserSerializer, 'Notification', 'Notification'),
    list=schema_list(UserSerializer, 'Notification', 'Notification'),
)
class NotificationView(ReadDeleteViewSet):
    """
    Notification Read and write view.
    """

    # Notification changes:
    Notification_changes = True
    # Basic API view parameters:
    queryset = NotificationModel.objects.all().order_by('-timestamp')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = NotificationSerializer
    # Django rest framework filters:
    filterset_class = NotificationFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
