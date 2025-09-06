# Django import:
from django.contrib import admin

# AlpenWegs import:
from assets.models.photo_model import PhotoModel
from assets.models.file_model import FileModel


@admin.register(PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    """
    Admin panel for managing PhotoModel objects.
    Provides list display, filters, search, and field organization.
    """

    model = PhotoModel
    list_display = (
        'id',
        'title',
        'file',
        'owner',
        'is_public',
        'created',
        'updated'
    )
    list_filter = (
        'is_public',
        'created',
        'updated'
    )
    search_fields = (
        'title',
        'description',
        'owner__email',
        'owner__first_name',
        'owner__last_name'
    )
    ordering = (
        '-created',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'title',
                    'description',
                    'file'
                )
            }
        ),
        (
            'Ownership', {
                'fields': (
                    'owner',
                    'is_public'
                )
            }
        ),
        (
            'Metadata', {
                'fields': (
                    'created',
                    'updated'
                )
            }
        ),
    )

    readonly_fields = ('created', 'updated')


@admin.register(FileModel)
class FileAdmin(admin.ModelAdmin):
    """
    Admin panel for managing FileModel objects.
    Provides list display, filters, search, and field organization.
    """

    model = FileModel
    list_display = (
        'id',
        'title',
        'file',
        'owner',
        'is_public',
        'created',
        'updated'
    )
    list_filter = (
        'is_public',
        'created',
        'updated'
    )
    search_fields = (
        'title',
        'description',
        'owner__email',
        'owner__first_name',
        'owner__last_name'
    )
    ordering = (
        '-created',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'title',
                    'description',
                    'file'
                )
            }
        ),
        (
            'Ownership', {
                'fields': (
                    'owner',
                    'is_public'
                )
            }
        ),
        (
            'Metadata', {
                'fields': (
                    'created',
                    'updated'
                )
            }
        ),
    )

    readonly_fields = ('created', 'updated')
