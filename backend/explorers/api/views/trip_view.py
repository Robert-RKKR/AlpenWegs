# AlpenWegs application import:
from explorers.api.serializers.trip_serializer import TripDetailedSerializer
from explorers.api.filters.trip_filter import TripFilter
from explorers.models.trip_model import TripModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_partial_update
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_destroy
from alpenwegs.ashared.api.schemas.schema_generators import schema_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_create
from alpenwegs.ashared.api.schemas.schema_generators import schema_list
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Trip Model API view class:
@extend_schema_view(
    partial_update=schema_partial_update(TripDetailedSerializer, 'Explorers', 'Trip'),
    retrieve=schema_retrieve(TripDetailedSerializer, 'Explorers', 'Trip'),
    destroy=schema_destroy(TripDetailedSerializer, 'Explorers', 'Trip'),
    update=schema_update(TripDetailedSerializer, 'Explorers', 'Trip'),
    create=schema_create(TripDetailedSerializer, 'Explorers', 'Trip'),
    list=schema_list(TripDetailedSerializer, 'Explorers', 'Trip'),
)
class TripView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Trip model.
    """

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = TripModel

    # Serializer class used for the view:
    serializer_class = TripDetailedSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = TripFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
