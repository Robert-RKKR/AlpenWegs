# AlpenWegs application import:
from compendiums.api.serializers.region_serializer import RegionDetailedSerializer
from compendiums.api.filters.region_filter import RegionFilter
from compendiums.models.region_model import RegionModel

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


# Region Model API view class:
@extend_schema_view(
    partial_update=schema_partial_update(RegionDetailedSerializer, 'Compendiums', 'Region'),
    retrieve=schema_retrieve(RegionDetailedSerializer, 'Compendiums', 'Region'),
    destroy=schema_destroy(RegionDetailedSerializer, 'Compendiums', 'Region'),
    update=schema_update(RegionDetailedSerializer, 'Compendiums', 'Region'),
    create=schema_create(RegionDetailedSerializer, 'Compendiums', 'Region'),
    list=schema_list(RegionDetailedSerializer, 'Compendiums', 'Region'),
)
class RegionView(ReadWriteViewSet):
    """
    Read-write API view for the Region model.
    """

    # Query used to collect objects for the view:
    queryset = RegionModel.objects.all().order_by('-created')

    # Serializer class used for the view:
    serializer_class = RegionDetailedSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = RegionFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
