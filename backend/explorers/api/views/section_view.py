# AlpenWegs application import:
from explorers.api.serializers.section_serializer import SectionDetailedSerializer
from explorers.api.filters.section_filter import SectionFilter
from explorers.models.section_model import SectionModel

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


# Section Model API view class:
@extend_schema_view(
    partial_update=schema_partial_update(SectionDetailedSerializer, 'Explorers', 'Section'),
    retrieve=schema_retrieve(SectionDetailedSerializer, 'Explorers', 'Section'),
    destroy=schema_destroy(SectionDetailedSerializer, 'Explorers', 'Section'),
    update=schema_update(SectionDetailedSerializer, 'Explorers', 'Section'),
    create=schema_create(SectionDetailedSerializer, 'Explorers', 'Section'),
    admin=schema_list(SectionDetailedSerializer, 'Explorers', 'Section'),
    list=schema_list(SectionDetailedSerializer, 'Explorers', 'Section'),
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

    # Serializer class used for the view:
    serializer_class = SectionDetailedSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = SectionFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
