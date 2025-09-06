# AlpenWegs application import:
from assets.api.serializers.photo_serializer import PhotoDetailedSerializer
from assets.api.filters.photo_filter import PhotoFilter
from assets.models.photo_model import PhotoModel

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


# Photo Model API view class:
@extend_schema_view(
    partial_update=schema_partial_update(PhotoDetailedSerializer, 'Assets', 'Photo'),
    retrieve=schema_retrieve(PhotoDetailedSerializer, 'Assets', 'Photo'),
    destroy=schema_destroy(PhotoDetailedSerializer, 'Assets', 'Photo'),
    update=schema_update(PhotoDetailedSerializer, 'Assets', 'Photo'),
    create=schema_create(PhotoDetailedSerializer, 'Assets', 'Photo'),
    list=schema_list(PhotoDetailedSerializer, 'Assets', 'Photo'),
)
class PhotoView(
    ReadWriteViewSet,
):
    """
    Read-write API views for the Photo model.
    """

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = PhotoModel

    # Serializer class used for the view:
    serializer_class = PhotoDetailedSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = PhotoFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
