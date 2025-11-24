# AlpenWegs application import:
from assets.api.serializers.photo_serializer import PhotoRepresentationSerializer
from assets.api.serializers.photo_serializer import PhotoDetailedSerializer
from assets.api.serializers.photo_serializer import PhotoRelationSerializer
from assets.api.filters.photo_filter import PhotoFilter
from assets.models.photo_model import PhotoModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Photo Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=PhotoRepresentationSerializer,
        detailed_schema=PhotoDetailedSerializer,
        relation_schema=PhotoRelationSerializer,
        application_repr='Assets',
        object_repr='Photo',
    )
)
class PhotoView(
    ReadWriteViewSet,
):
    """
    Read-write API views for the Photo model.
    """

    # Log model changes:
    log_changes = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = PhotoModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = PhotoModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = PhotoDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = PhotoRepresentationSerializer
    detailed_serializer_class = PhotoDetailedSerializer
    relation_serializer_class = PhotoRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = PhotoFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
