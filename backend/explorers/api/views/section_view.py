# AlpenWegs application import:
from explorers.api.serializers.section_serializer import SectionRepresentationSerializer
from explorers.api.serializers.section_serializer import SectionDetailedSerializer
from explorers.api.serializers.section_serializer import SectionRelationSerializer
from explorers.api.serializers.section_serializer import SectionGpxSerializer
from explorers.api.filters.section_filter import SectionFilter
from explorers.models.section_model import SectionModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_create
from drf_spectacular.utils import extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


# Section Model API view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=SectionRepresentationSerializer,
        detailed_schema=SectionDetailedSerializer,
        relation_schema=SectionRelationSerializer,
        application_repr='Explorers',
        object_repr='Section',
        **{
            'gpx': schema_create(
                application_repr='Explorers',
                response_schema=SectionDetailedSerializer,
                request_schema=SectionGpxSerializer,
                object_repr='Section',
            )
        }
    )
)
class SectionView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Section model.
    """

    # Create change notifications:
    send_notification = False
    create_change = True

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
    gpx_serializer_class = SectionGpxSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = SectionFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'

    @action(detail=False, methods=['post'], url_path='gpx')
    def gpx(self,
        request,
        pk=None,
    ):
        """
        Create a new Section instance from provided GPX data.
        """

        # Collect user from request:
        user = getattr(request, 'user', False)

        # Collect a new object GPX serializer:
        input_serializer = self._get_serializer(
            serializer_name='gpx',
            data=request.data,
        )
        
        # Validate created serializer:
        input_serializer.is_valid(raise_exception=True)
        # Add creator to serializer data if available:
        input_serializer.save(creator=user)
        # Save a new instance based on validated serializer data:
        instance = input_serializer.save()

        # Collect a new object output serializer:
        output_serializer = self._get_serializer(
            serializer_name='detailed',
            instance=instance,
        )

        # Return (201 HTTP - Created) response:
        return Response(
            data=output_serializer.data,
            status=status.HTTP_201_CREATED,
        )
