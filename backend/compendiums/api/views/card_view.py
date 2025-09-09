# AlpenWegs application import:
from compendiums.api.serializers.card_serializer import CardRepresentationSerializer
from compendiums.api.serializers.card_serializer import CardDetailedSerializer
from compendiums.api.serializers.card_serializer import CardRelationSerializer
from compendiums.api.filters.card_filter import CardFilter
from compendiums.models.card_model import CardModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_partial_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_representation
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_destroy
from alpenwegs.ashared.api.schemas.schema_generators import schema_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_create
from alpenwegs.ashared.api.schemas.schema_generators import schema_list
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# API import:
from drf_spectacular.utils import extend_schema_view


# Card Model API view class:
@extend_schema_view(
    representation=schema_representation(CardDetailedSerializer, 'Compendiums', 'Card'),
    partial_update=schema_partial_update(CardDetailedSerializer, 'Compendiums', 'Card'),
    retrieve=schema_retrieve(CardDetailedSerializer, 'Compendiums', 'Card'),
    destroy=schema_destroy(CardDetailedSerializer, 'Compendiums', 'Card'),
    update=schema_update(CardDetailedSerializer, 'Compendiums', 'Card'),
    create=schema_create(CardDetailedSerializer, 'Compendiums', 'Card'),
    admin=schema_list(CardDetailedSerializer, 'Compendiums', 'Card'),
    list=schema_list(CardDetailedSerializer, 'Compendiums', 'Card'),
)
class CardView(
    ReadWriteViewSet,
):
    """
    Read-write API view for the Card model.
    """

    # Queryset for the view (Legacy, required by DRF):
    queryset = CardModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = CardModel
    # Serializer class (Legacy, required by DRF):
    serializer_class = CardDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = CardRepresentationSerializer
    detailed_serializer_class = CardDetailedSerializer
    relation_serializer_class = CardRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = CardFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
