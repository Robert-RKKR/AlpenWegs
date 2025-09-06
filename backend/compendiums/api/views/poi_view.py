# AlpenWegs application import:
from compendiums.api.serializers.poi_serializer import PoiDetailedSerializer
from compendiums.api.filters.poi_filter import PoiFilter
from compendiums.models.poi_model import PoiModel

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


# PoI Model API view class:
@extend_schema_view(
    partial_update=schema_partial_update(PoiDetailedSerializer, 'Compendiums', 'Poi'),
    retrieve=schema_retrieve(PoiDetailedSerializer, 'Compendiums', 'Poi'),
    destroy=schema_destroy(PoiDetailedSerializer, 'Compendiums', 'Poi'),
    update=schema_update(PoiDetailedSerializer, 'Compendiums', 'Poi'),
    create=schema_create(PoiDetailedSerializer, 'Compendiums', 'Poi'),
    list=schema_list(PoiDetailedSerializer, 'Compendiums', 'Poi'),
)
class PoiView(ReadWriteViewSet):
    """
    Read-write API view for the PoI model.
    """

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = PoiModel

    # Serializer class used for the view:
    serializer_class = PoiDetailedSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = PoiFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
