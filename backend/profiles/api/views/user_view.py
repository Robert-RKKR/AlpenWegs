# AlpenWegs application import:
from profiles.api.serializers.user_serializer import UserRepresentationSerializer
from profiles.api.serializers.user_serializer import UserDetailedSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from profiles.api.filters.user_filter import UserFilter
from profiles.models.user_model import UserModel

# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_full_generator import red_write_schema
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# Drf spectacular import:
from drf_spectacular.utils import extend_schema_view


# User Model api view class:
@extend_schema_view(
    **red_write_schema(
        representation_schema=UserRepresentationSerializer,
        detailed_schema=UserDetailedSerializer,
        relation_schema=UserRelationSerializer,
        application_repr='Profiles',
        object_repr='User',
    )
)
class UserView(
    ReadWriteViewSet,
):
    """
    User Read and write view.
    """

    # Queryset for the view (Legacy, required by DRF):
    queryset = UserModel.objects.all()

    # Model and query ordering used for the view:
    query_ordering = '-created'
    query_model = UserModel

    # Serializer class (Legacy, required by DRF):
    serializer_class = UserDetailedSerializer

    # Serializer class used for the view:
    representation_serializer_class = UserRepresentationSerializer
    detailed_serializer_class = UserDetailedSerializer
    relation_serializer_class = UserRelationSerializer

    # Pagination class used for the view:
    pagination_class = BaseSmallPaginator

    # Filter classes used for the view:
    filterset_class = UserFilter

    # Ordering filter parameters:
    ordering_fields = '__all__'

    # Search filter parameters:
    search_fields = '__all__'
