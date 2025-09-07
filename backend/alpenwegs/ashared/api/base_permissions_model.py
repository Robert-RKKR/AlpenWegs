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
        'GET': 'view',
        'HEAD': 'view',
        'OPTIONS': 'view',
        'POST': 'add',
        'PUT': 'change',
        'PATCH': 'change',
        'DELETE': 'delete',
    }

    def has_permission(self,
        request,
        view,
    ):
        
        # Check is user is superuser:
        if request.user and request.user.is_superuser:
            # Allow access for superusers:
            return True

        # Check if user is authenticated:
        if not request.user or not request.user.is_authenticated:
            # Deny access for unauthenticated users:
            return False
        
        # Collect action:
        action = self.perms_map.get(request.method)
        # Check if action has been collected:
        if not action:
            # Deny access if no permission is defined for the method:
            return False

        # Allow methods that will be verified in has_object_permission:
        if action not in ['view', 'add']:
            # Allow action:
            return True

        # Get model class from view's queryset:
        model_cls = getattr(
            getattr(view, 'queryset', None), 'model', None
        )
        # Check if model class is available:
        if not model_cls:
            # Deny access if model class is not found:
            return False
        # Collect details info about the class model:
        app_label = model_cls._meta.app_label
        model_name = model_cls._meta.model_name

        # Collect action code name:
        if action == 'view':

            # Check if view is admin view:
            if hasattr(view, 'action') and view.action == 'admin':
                # Create access code for admin view action:
                codename = f'{app_label}.view_all_{model_name}'
            
            else:
                # Create access code for other view actions:
                codename = f'{app_label}.view_own_{model_name}'

        else:
            # Create access code for add action:
            codename = f'{app_label}.add_own_{model_name}'

        # print(f'\n\napp_label: {app_label}')
        # print(f'model_name: {model_name}')
        # print(f'model_cls: {model_cls}')
        # print(f'action: {action}')
        # print(f'codename: {codename}\n\n')

        # Return whether the user has the required permission:
        return request.user.has_perm(codename)

    def has_object_permission(self,
        request,
        view,
        obj,
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
