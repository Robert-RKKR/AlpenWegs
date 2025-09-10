# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_representation
from alpenwegs.ashared.api.schemas.schema_generators import schema_partial_update
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_destroy
from alpenwegs.ashared.api.schemas.schema_generators import schema_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_create
from alpenwegs.ashared.api.schemas.schema_generators import schema_list
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# AlpenWegs application import:
from profiles.api.serializers.user_serializer import UserRepresentationSerializer
from profiles.api.serializers.user_serializer import UserDetailedSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from profiles.api.filters.user_filter import UserFilter
from profiles.models.user_model import UserModel

# Drf spectacular import:
from drf_spectacular.utils import extend_schema_view


# User Model api view class:
@extend_schema_view(
    representation=schema_representation(UserDetailedSerializer, 'Assets', 'File'),
    partial_update=schema_partial_update(UserDetailedSerializer, 'ProUsers', 'User'),
    retrieve=schema_retrieve(UserDetailedSerializer, 'ProUsers', 'User'),
    destroy=schema_destroy(UserDetailedSerializer, 'ProUsers', 'User'),
    update=schema_update(UserDetailedSerializer, 'ProUsers', 'User'),
    create=schema_create(UserDetailedSerializer, 'ProUsers', 'User'),
    admin=schema_list(UserDetailedSerializer, 'ProUsers', 'User'),
    list=schema_list(UserDetailedSerializer, 'ProUsers', 'User'),
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
