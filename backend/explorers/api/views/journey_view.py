# AlpenWegs application import:
from explorers.api.serializers.journey_serializer import JourneyRepresentationSerializer
from explorers.api.serializers.journey_serializer import JourneyDetailedSerializer
from explorers.api.serializers.journey_serializer import JourneyRelationSerializer
from explorers.api.filters.journey_filter import JourneyFilter
from explorers.models.journey_model import JourneyModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Journey Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=JourneyRepresentationSerializer,
        detailed_schema=JourneyDetailedSerializer,
        relation_schema=JourneyRelationSerializer,
        application_repr='Explorers',
        object_repr='Journey',
    )
)
class JourneyView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Journey model.
    """

    # Log model changes:
    log_changes = True

    # Queryset for the view (Legacy, required by DRF):
    queryset = JourneyModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = JourneyModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = JourneyDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = JourneyRepresentationSerializer
    detailed_serializer_class = JourneyDetailedSerializer
    relation_serializer_class = JourneyRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = JourneyFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
