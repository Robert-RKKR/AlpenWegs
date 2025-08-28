# Alpenwegs import:
from alpenwegs.ashared.models.creator_model import BaseCreatorModel

# Rest framework import:
from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

# Alpenwegs application import:
from profiles.models.user_model import UserModel


# Base Permission Model:
class BasePermissionsModel(
    BasePermission,
):
    """
    Replacement for DjangoModelPermissions.
    - Users with `read_only` can only GET/list/retrieve.
    - Users with `read_write` can GET/list/retrieve and also create/update/delete.
    - Superusers always bypass.
    - Object-level rule: only owners can update/delete their own objects.
    """

    perms_map = {
        'GET':     'view',
        'HEAD':    'view',
        'OPTIONS': 'view',
        'POST':    'add',
        'PUT':     'change',
        'PATCH':   'change',
        'DELETE':  'delete',
    }

    def has_permission(self,
        request,
        view
    ):
        
        # Check is user is superuser:
        if request.user and request.user.is_superuser:
            # Allow access for superusers:
            return True

        # Check if user is authenticated:
        if not request.user or not request.user.is_authenticated:
            # Deny access for unauthenticated users:
            return False

        # Get model class from view's queryset:
        model_cls = getattr(getattr(view, 'queryset', None), 'model', None)
        # Check if model class is available:
        if not model_cls:
            # Deny access if model class is not found:
            return False
        # Collect details info about the class model:
        app_label = model_cls._meta.app_label
        model_name = model_cls._meta.model_name

        # Get required permission based on HTTP method:
        required_perm = self.perms_map.get(request.method)
        # Check if required permission is defined:
        if not required_perm:
            # Deny access if no permission is defined for the method:
            return False

        # Create full permission codename:
        codename = f'{app_label}.{required_perm}_{model_name}'

        # Return whether the user has the required permission:
        return request.user.has_perm(codename)

    def has_object_permission(self,
        request,
        view,
        obj
    ):

        # Superusers bypass
        if request.user.is_superuser:
            return True
        
        

        # Write actions → only if owner
        return getattr(obj, 'created_by_id', None) == request.user.id

    def has_object_permission(self,
        request,
        view,
        obj
    ):

        # Collect user from request:
        user = request.user

        # Superusers bypass everything:
        if getattr(user, 'is_superuser', False):
            return True
        
        # Check if user is instance of UserModel:
        if isinstance(obj, UserModel):
            # Check if the object is the same as the user:
            if obj.pk == user.pk:
                # Users can manage their own user object:
                return True
            else:
                # Deny access to other user objects:
                return False

        # Check if model is instance of BaseCreatorModel:
        elif isinstance(obj, BaseCreatorModel):
            # Check if user is the creator of the object:
            if obj.creator_pk == user.pk:
                # Owner can run all actions on instance:
                return True
            
            # If user is not owner allow safe methods on public objects:
            if obj.is_public:
                # Allow safe methods on public objects:
                return request.method in SAFE_METHODS
            
            # In any other case deny access:
            return False

        # For other models, deny access by default:
        return False
