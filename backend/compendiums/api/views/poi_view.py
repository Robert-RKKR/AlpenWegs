# AlpenWegs application import:
from compendiums.api.serializers.poi_serializer import PoiRepresentationSerializer
from compendiums.api.serializers.poi_serializer import PoiWhereUsedSerializer
from compendiums.api.serializers.poi_serializer import PoiDetailedSerializer
from compendiums.api.serializers.poi_serializer import PoiRelationSerializer
from compendiums.api.filters.poi_filter import PoiFilter
from compendiums.models.poi_model import PoiModel

# AlpenWegs import:
from alpenwegs.ashared.api.mixins.base_where_used_mixin import BaseWhereUsedModelMixin
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# PoI Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=PoiRepresentationSerializer,
        where_used_schema=PoiWhereUsedSerializer,
        detailed_schema=PoiDetailedSerializer,
        relation_schema=PoiRelationSerializer,
        application_repr='Compendiums',
        object_repr='Poi',
    )
)
class PoiView(
    ReadWriteViewSet,
    BaseWhereUsedModelMixin,
):
    """
    Read-write API view for the PoI model.
    """

    # Log model changes:
    log_changes = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = PoiModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = PoiModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = PoiDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = PoiRepresentationSerializer
    where_used_serializer_class = PoiWhereUsedSerializer
    detailed_serializer_class = PoiDetailedSerializer
    relation_serializer_class = PoiRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = PoiFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
