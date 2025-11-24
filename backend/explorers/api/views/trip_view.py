# AlpenWegs application import:
from explorers.api.serializers.trip_serializer import TripRepresentationSerializer
from explorers.api.serializers.trip_serializer import TripDetailedSerializer
from explorers.api.serializers.trip_serializer import TripRelationSerializer
from explorers.api.filters.trip_filter import TripFilter
from explorers.models.trip_model import TripModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Trip Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=TripRepresentationSerializer,
        detailed_schema=TripDetailedSerializer,
        relation_schema=TripRelationSerializer,
        application_repr='Explorers',
        object_repr='Trip',
    )
)
class TripView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Trip model.
    """

    # Create change notifications:
    send_notification = False
    create_change = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = TripModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = TripModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = TripDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = TripRepresentationSerializer
    detailed_serializer_class = TripDetailedSerializer
    relation_serializer_class = TripRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = TripFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
