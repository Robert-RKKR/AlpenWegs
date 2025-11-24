# AlpenWegs application import:
from explorers.api.serializers.route_serializer import RouteRepresentationSerializer
from explorers.api.serializers.route_serializer import RouteDetailedSerializer
from explorers.api.serializers.route_serializer import RouteRelationSerializer
from explorers.api.filters.route_filter import RouteFilter
from explorers.models.route_model import RouteModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Route Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=RouteRepresentationSerializer,
        detailed_schema=RouteDetailedSerializer,
        relation_schema=RouteRelationSerializer,
        application_repr='Explorers',
        object_repr='Route',
    )
)
class RouteView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Route model.
    """

    # Create change notifications:
    send_notification = False
    create_change = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = RouteModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = RouteModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = RouteDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = RouteRepresentationSerializer
    detailed_serializer_class = RouteDetailedSerializer
    relation_serializer_class = RouteRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = RouteFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
