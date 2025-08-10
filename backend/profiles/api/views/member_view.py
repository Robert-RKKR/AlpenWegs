# AlpenWegs import:
from alpenwegs.ashared.api.base_model_viewset import ReadWriteViewSet
from alpenwegs.ashared.api.base_pagination import BaseSmallPaginator

# AlpenWegs application import:
from profiles.api.serializers.member_serializer import MemberSerializer
from profiles.api.filters.member_filter import MemberFilter
from profiles.models.member_model import MemberModel

# Drf spectacular import:
from drf_spectacular.utils import extend_schema_view
from drf_spectacular.utils import extend_schema


# Member Model api view class:
@extend_schema_view(
    list=extend_schema(tags=['Profiles - Member']),
    retrieve=extend_schema(tags=['Profiles - Member']),
    create=extend_schema(tags=['Profiles - Member']),
    update=extend_schema(tags=['Profiles - Member']),
    partial_update=extend_schema(tags=['Profiles - Member']),
    destroy=extend_schema(tags=['Profiles - Member']),
)
class MemberView(ReadWriteViewSet):
    """
    Member Read and write view.
    """

    # Member changes:
    log_changes = True
    # Basic API view parameters:
    queryset = MemberModel.objects.all().order_by('-created')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = MemberSerializer
    # Django rest framework filters:
    filterset_class = MemberFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
