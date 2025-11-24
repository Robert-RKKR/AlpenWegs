# AlpenWegs application import:
from assets.api.serializers.file_serializer import FileRepresentationSerializer
from assets.api.serializers.file_serializer import FileDetailedSerializer
from assets.api.serializers.file_serializer import FileRelationSerializer
from assets.api.filters.file_filter import FileFilter
from assets.models.file_model import FileModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# File Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=FileRepresentationSerializer,
        detailed_schema=FileDetailedSerializer,
        relation_schema=FileRelationSerializer,
        application_repr='Assets',
        object_repr='File',
    )
)
class FileView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the File model.
    """

    # Log model changes:
    log_changes = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = FileModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = FileModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = FileDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = FileRepresentationSerializer
    detailed_serializer_class = FileDetailedSerializer
    relation_serializer_class = FileRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = FileFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
