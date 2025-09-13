# AlpenWegs application import:
from explorers.api.serializers.section_serializer import SectionRepresentationSerializer
from explorers.api.serializers.section_serializer import SectionDetailedSerializer
from explorers.api.serializers.section_serializer import SectionRelationSerializer
from explorers.api.filters.section_filter import SectionFilter
from explorers.models.section_model import SectionModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Section Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=SectionRepresentationSerializer,
        detailed_schema=SectionDetailedSerializer,
        relation_schema=SectionRelationSerializer,
        application_repr='Explorers',
        object_repr='Section',
    )
)
class SectionView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Section model.
    """

    # Queryset for the view (Legacy, required by DRF):
    queryset = SectionModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = SectionModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = SectionDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = SectionRepresentationSerializer
    detailed_serializer_class = SectionDetailedSerializer
    relation_serializer_class = SectionRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = SectionFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
