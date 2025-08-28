# AlpenWegs import:
from alpenwegs.ashared.api.schemas.schema_generators import schema_partial_update
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.schemas.schema_generators import schema_retrieve
from alpenwegs.ashared.api.schemas.schema_generators import schema_destroy
from alpenwegs.ashared.api.schemas.schema_generators import schema_update
from alpenwegs.ashared.api.schemas.schema_generators import schema_create
from alpenwegs.ashared.api.schemas.schema_generators import schema_list
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet

# AlpenWegs application import:
from profiles.api.serializers.user_serializer import UserSerializer
from profiles.api.filters.user_filter import UserFilter
from profiles.models.user_model import UserModel

# Drf spectacular import:
from drf_spectacular.utils import extend_schema_view


# User Model api view class:
@extend_schema_view(
    partial_update=schema_partial_update(UserSerializer, 'Profiles', 'User'),
    retrieve=schema_retrieve(UserSerializer, 'Profiles', 'User'),
    destroy=schema_destroy(UserSerializer, 'Profiles', 'User'),
    update=schema_update(UserSerializer, 'Profiles', 'User'),
    create=schema_create(UserSerializer, 'Profiles', 'User'),
    list=schema_list(UserSerializer, 'Profiles', 'User'),
)
class UserView(ReadWriteViewSet):
    """
    User Read and write view.
    """

    # User changes:
    log_changes = True
    # Basic API view parameters:
    queryset = UserModel.objects.all().order_by('-created')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = UserSerializer
    # Django rest framework filters:
    filterset_class = UserFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
