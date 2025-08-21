# Django - admin import:
from django.contrib import admin

# AlpenWegsbase import:
from alpenwegs.ashared.admins.based_admin import BaseAdmin

# AlpenWegs application import:
from notifications.models.notification_model import NotificationModel
from notifications.models.change_log_model import ChangeLogModel


@admin.register(NotificationModel)
class NotificationAdmin(BaseAdmin):

    list_display = (
        'pk', 'timestamp', 'severity', 'task_id', 'message',
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'severity',
    )
    search_fields = (
        'message', 'task_id',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('severity', 'task_id', 'message', 'url')
        }),
    )
    readonly_fields = (
        'timestamp', 'severity', 'task_id', 'message', 'url'
    )
    empty_value_display = '--None--'


@admin.register(ChangeLogModel)
class ChangLogAdmin(BaseAdmin):

    list_display = (
        'pk', 'user', 'timestamp', 'action_type', 'model_name',
        'object_representation', 'object_id',
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        'app_name', 'user', 'model_name', 'action_type',
        'after',
    )
    search_fields = (
        'object_id', 'after',
    )
    fieldsets = (
        ('Basic information', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('user', 'app_name', 'model_name',
                'object_representation', 'object_id',)
        }),
        ('Object Json representation', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('after',),
        }),
    )
    readonly_fields = (
        'user', 'timestamp', 'action_type', 'user', 'app_name',
        'object_representation', 'after', 'object_id', 'model_name',
    )
    empty_value_display = '--None--'
