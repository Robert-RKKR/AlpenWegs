# AlpenWegs import:
from alpenwegs.ashared.api.mixins.base_list_representation_mixin import BaseListRepresentationModelMixin
from alpenwegs.ashared.api.mixins.base_list_admin_mixin import BaseListAdminModelMixin
from alpenwegs.ashared.api.mixins.base_retrieve_mixin import BaseRetrieveModelMixin
from alpenwegs.ashared.api.mixins.base_destroy_mixin import BaseDestroyModelMixin
from alpenwegs.ashared.api.mixins.base_update_mixin import BaseUpdateModelMixin
from alpenwegs.ashared.api.mixins.base_create_mixin import BaseCreateModelMixin
from alpenwegs.ashared.api.base_permissions_model import BasePermissionsModel
from alpenwegs.ashared.api.mixins.base_list_mixin import BaseListModelMixin

# Rest framework import:
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework import viewsets


# Base ModelViewSet model:
class BaseViewSet(
    viewsets.GenericViewSet,
):
    """
    BaseViewSet provides foundational configuration for all ModelViewSets used
    in the AlpenWegs project. It integrates authentication, permissions, and
    filtering systems to create standardized behavior across views.

    Authentication:
        Uses both Session and Token-based authentication.
    Permissions:
        Leverages DjangoModelPermissions to enforce per-object permission checks.
    Filters:
        Supports filtering with Django's built-in filters, search functionality, 
        and ordering based on query parameters.

    Attributes:
        log_changes:
            Boolean flag to track if changes are logged for auditing purposes.
        metadata:
            Custom metadata to be used for view customization or additional 
            contextual information in API responses.
    """

    # Initiate empty QuerySet:
    queryset = None

    # Authentication and permissions:
    authentication_classes = [
        JWTAuthentication,
    ]
    permission_classes = [
        BasePermissionsModel,
    ]

    # Django rest framework filters:
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # Create change notifications:
    send_notification = False
    create_change = False
    
    metadata = {
        'my_custom_option': 'Some custom option',
        'my_other_option': 'Another custom option',
    }

    def metadata(self, request):
        metadata = super().metadata(request)
        metadata['my_custom_option'] = 'Modified custom option'
        return metadata


# All AlpenWegs ModelViewSet models:
class ReadWriteViewSet(
    BaseViewSet,
    BaseListRepresentationModelMixin,
    BaseListAdminModelMixin,
    BaseRetrieveModelMixin,
    BaseDestroyModelMixin,
    BaseCreateModelMixin,
    BaseUpdateModelMixin,
    BaseListModelMixin,
):
    """
    ReadWriteViewSet provides full CRUD (Create, Retrieve, Update, Delete) 
    functionality for models. This class integrates all the behavior needed 
    for complete management of model instances, supporting creation, retrieval,
    modification, and deletion.
    """

    pass


class ReadWriteNoListViewSet(
    BaseViewSet,
    BaseListRepresentationModelMixin,
    BaseListAdminModelMixin,
    BaseRetrieveModelMixin,
    BaseDestroyModelMixin,
    BaseCreateModelMixin,
    BaseUpdateModelMixin,
):
    """
    ReadWriteNoListViewSet provides full CRUD (Create, Retrieve, Update, Delete)
    functionality for models without list access. This class integrates all the behavior needed
    for complete management of model instances, supporting creation, retrieval,
    modification, and deletion.
    """

    pass
    


class ReadOnlyViewSet(
    BaseViewSet,
    BaseListRepresentationModelMixin,
    BaseListAdminModelMixin,
    BaseRetrieveModelMixin,
    BaseListModelMixin,
):
    """
    ReadOnlyViewSet restricts the view to read-only operations. It allows 
    fetching a list of model instances or retrieving a single instance by ID, 
    but it disallows any modification (create, update, delete) actions.

    """

    pass


class ReadDeleteViewSet(
    BaseViewSet,
    BaseListRepresentationModelMixin,
    BaseListAdminModelMixin,
    BaseRetrieveModelMixin,
    BaseDestroyModelMixin,
    BaseListModelMixin,
):
    """
    ReadDeleteViewSet allows retrieval and deletion of model instances but 
    restricts creation and updating of models. It is designed for cases where
    only read and delete functionality is needed.
    """
    
    pass


class RetrieveOnlyViewSet(
    BaseViewSet,
    BaseRetrieveModelMixin,
):
    """
    RetrieveOnlyViewSet is a minimal viewset that restricts operations 
    to retrieving individual instances only. No list, create, update, or 
    delete functionality is provided.
    """

    pass
    

class ReadEditViewSet(
    BaseViewSet,
    BaseListRepresentationModelMixin,
    BaseListAdminModelMixin,
    BaseRetrieveModelMixin,
    BaseUpdateModelMixin,
    BaseListModelMixin,
):
    """
    ReadEditViewSet allows read and update operations. This viewset can 
    retrieve a list of instances, retrieve a single instance by ID, and 
    update existing instances but prevents creation and deletion.
    """

    pass
