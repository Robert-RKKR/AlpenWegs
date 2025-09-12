# AlpenWegs application import:
from compendiums.api.serializers.region_serializer import RegionRepresentationSerializer
from compendiums.api.serializers.region_serializer import RegionDetailedSerializer
from compendiums.api.serializers.region_serializer import RegionRelationSerializer
from compendiums.api.filters.region_filter import RegionFilter
from compendiums.models.region_model import RegionModel
 
# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Region Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=RegionRepresentationSerializer,
        detailed_schema=RegionDetailedSerializer,
        relation_schema=RegionRelationSerializer,
        application_repr='Compendiums',
        object_repr='Region',
    )
)
class RegionView(ReadWriteViewSet):
    """
    Read-write API view for the Region model.
    """

    # Log model changes:
    log_changes = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = RegionModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = RegionModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = RegionDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = RegionRepresentationSerializer
    detailed_serializer_class = RegionDetailedSerializer
    relation_serializer_class = RegionRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = RegionFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
