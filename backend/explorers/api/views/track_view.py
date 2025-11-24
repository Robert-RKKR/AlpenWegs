# AlpenWegs application import:
from explorers.api.serializers.track_serializer import TrackRepresentationSerializer
from explorers.api.serializers.track_serializer import TrackDetailedSerializer
from explorers.api.serializers.track_serializer import TrackRelationSerializer
from explorers.api.filters.track_filter import TrackFilter
from explorers.models.track_model import TrackModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Track Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=TrackRepresentationSerializer,
        detailed_schema=TrackDetailedSerializer,
        relation_schema=TrackRelationSerializer,
        application_repr='Explorers',
        object_repr='Track',
    )
)
class TrackView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Track model.
    """

    # Create change notifications:
    send_notification = False
    create_change = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = TrackModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = TrackModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = TrackDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = TrackRepresentationSerializer
    detailed_serializer_class = TrackDetailedSerializer
    relation_serializer_class = TrackRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = TrackFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
