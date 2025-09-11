# AlpenWegs application import:
from explorers.api.serializers.route_serializer import RouteRepresentationSerializer
from explorers.api.serializers.route_serializer import RouteDetailedSerializer
from explorers.api.serializers.route_serializer import RouteRelationSerializer
from explorers.api.filters.route_filter import RouteFilter
from explorers.models.route_model import RouteModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_partial_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_representation
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_destroy
from alpenwegs.ashared.api.schemas.schema_generators import schema_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_create
from alpenwegs.ashared.api.schemas.schema_generators import schema_admin
from alpenwegs.ashared.api.schemas.schema_generators import schema_list
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Route Model API view class:
@extend_schema_view(
    representation=schema_representation(RouteDetailedSerializer, 'Explorers', 'Route'),
    partial_update=schema_partial_update(RouteDetailedSerializer, 'Explorers', 'Route'),
    retrieve=schema_retrieve(RouteDetailedSerializer, 'Explorers', 'Route'),
    destroy=schema_destroy(RouteDetailedSerializer, 'Explorers', 'Route'),
    update=schema_update(RouteDetailedSerializer, 'Explorers', 'Route'),
    create=schema_create(RouteDetailedSerializer, 'Explorers', 'Route'),
    admin=schema_admin(RouteDetailedSerializer, 'Explorers', 'Route'),
    list=schema_list(RouteDetailedSerializer, 'Explorers', 'Route'),
)
class RouteView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Route model.
    """

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
