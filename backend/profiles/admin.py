from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

@admin.register(UserModel)
class MemberAdmin(UserAdmin):
    model = UserModel
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gender')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name', 'middle_name', 'last_name',
                'phone_number', 'gender', 'birthday',
                'height', 'weight',
                'location', 'location_name',
            )
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created', 'updated')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )

    readonly_fields = ('last_login', 'created', 'updated')
