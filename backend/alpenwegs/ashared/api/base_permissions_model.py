# Rest framework import:
from rest_framework.permissions import BasePermission, SAFE_METHODS


# Base Premission Model:
class BasePermissionsModel(BasePermission):
    """
    Replacement for DjangoModelPermissions.
    - Users with `read_only` can only GET/list/retrieve.
    - Users with `read_write` can GET/list/retrieve and also create/update/delete.
    - Superusers always bypass.
    - Object-level rule: only owners can update/delete their own objects.
    """

    perms_map = {
        'GET': 'read_only',
        'OPTIONS': 'read_only',
        'HEAD': 'read_only',
        'POST': 'read_write',
        'PUT': 'read_write',
        'PATCH': 'read_write',
        'DELETE': 'read_write',
    }

    def has_permission(self, request, view):
        # Superusers bypass all checks
        if request.user and request.user.is_superuser:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        model_cls = getattr(getattr(view, 'queryset', None), 'model', None)
        if not model_cls:
            return False

        required_perm = self.perms_map.get(request.method)
        if not required_perm:
            return False

        app_label = model_cls._meta.app_label
        model_name = model_cls._meta.model_name
        codename = f"{app_label}.{required_perm}_{model_name}"

        return request.user.has_perm(codename)

    def has_object_permission(self, request, view, obj):
        # Safe methods are always allowed if user has read_only
        if request.method in SAFE_METHODS:
            return True

        # Superusers bypass
        if request.user.is_superuser:
            return True

        # Write actions → only if owner
        return getattr(obj, "created_by_id", None) == request.user.id
