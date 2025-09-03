# Django import:
from django.contrib.auth.admin import GroupAdmin as DjangoGroupAdmin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib import admin

# AlpenWegs import:
from profiles.models.group_model import GroupModel
from profiles.models.user_model import UserModel


@admin.register(UserModel)
class UserAdmin(DjangoUserAdmin):
    """
    Admin panel for the custom UserModel.
    Extends Django’s default UserAdmin so you still get the
    user management features.
    """

    model = UserModel
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active'
    )
    list_filter = (
        'is_staff',
        'is_active',
        'gender'
    )
    search_fields = (
        'email',
        'first_name',
        'last_name'
    )
    ordering = (
        '-created',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'email',
                    'password'
                )
            }
        ),
        (
            'Personal info', {
                'fields': (
                    'first_name',
                    'middle_name',
                    'last_name',
                    'phone_number',
                    'gender',
                    'birthday',
                    'height',
                    'weight',
                    'location',
                    'location_name',
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                )
            }
        ),
        (
            'Important dates', {
                'fields': (
                    'last_login',
                    'created',
                    'updated'
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'email',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_superuser',
                    'is_active'
                ),
            }
        ),
    )

    readonly_fields = ('last_login', 'created', 'updated')


@admin.register(GroupModel)
class GroupAdmin(DjangoGroupAdmin):
    """
    Admin panel for the custom GroupModel.
    Extends Django’s default GroupAdmin so you still get the
    permissions selection widget and filtering UI.
    """

    model = GroupModel
    filter_horizontal = (
        'permissions',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'name',
    )
