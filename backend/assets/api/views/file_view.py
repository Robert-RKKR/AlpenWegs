# AlpenWegs application import:
from assets.api.serializers.file_serializer import FileDetailedSerializer
from assets.api.filters.file_filter import FileFilter
from assets.models.file_model import FileModel

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


# File Model API view class:
@extend_schema_view(
    partial_update=schema_partial_update(FileDetailedSerializer, 'Assets', 'File'),
    retrieve=schema_retrieve(FileDetailedSerializer, 'Assets', 'File'),
    destroy=schema_destroy(FileDetailedSerializer, 'Assets', 'File'),
    update=schema_update(FileDetailedSerializer, 'Assets', 'File'),
    create=schema_create(FileDetailedSerializer, 'Assets', 'File'),
    admin=schema_list(FileDetailedSerializer, 'Assets', 'File'),
    list=schema_list(FileDetailedSerializer, 'Assets', 'File'),
)
class FileView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the File model.
    """

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = FileModel

    # Serializer class used for the view:
    serializer_class = FileDetailedSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = FileFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
