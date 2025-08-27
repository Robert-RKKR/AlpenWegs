# AlpenWegs import:
from alpenwegs.ashared.api.base_response_pagination import BaseSmallPaginator
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet
from alpenwegs.ashared.api.schema_generators import schema_retrieve

# AlpenWegs application import:
from profiles.api.serializers.user_serializer import UserSerializer
from profiles.api.filters.user_filter import UserFilter
from profiles.models.user_model import UserModel

# Drf spectacular import:
from drf_spectacular.utils import extend_schema_view
from drf_spectacular.utils import extend_schema

# User Model api view class:
@extend_schema_view(
    list=extend_schema(tags=['Profiles - User']),
    retrieve=schema_retrieve(UserSerializer, 'Profiles', 'User'),
    create=extend_schema(tags=['Profiles - User']),
    update=extend_schema(tags=['Profiles - User']),
    partial_update=extend_schema(tags=['Profiles - User']),
    destroy=extend_schema(tags=['Profiles - User']),
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
