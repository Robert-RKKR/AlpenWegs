# Django import:
from django.contrib import admin

# AlpenWegs import:
from explorers.models.route_model import RouteModel
from explorers.models.trip_model import TripModel
from explorers.models.section_model import SectionModel


@admin.register(RouteModel)
class RouteAdmin(admin.ModelAdmin):
    """
    Admin panel for managing RouteModel objects.
    """

    model = RouteModel
    list_display = (
        'id',
        'name',
        'region',
        'difficulty',
        'distance',
        'ascent',
        'descent',
        'created',
        'updated'
    )
    list_filter = (
        'difficulty',
        'region',
        'created',
        'updated'
    )
    search_fields = (
        'name',
        'description',
        'region__name'
    )
    ordering = (
        'name',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    'slug',
                    'description'
                )
            }
        ),
        (
            'Route data', {
                'fields': (
                    'distance',
                    'ascent',
                    'descent',
                    'duration',
                    'difficulty'
                )
            }
        ),
        (
            'Relations', {
                'fields': (
                    'region',
                    'gpx_file'
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


@admin.register(TripModel)
class TripAdmin(admin.ModelAdmin):
    """
    Admin panel for managing TripModel objects.
    """

    model = TripModel
    list_display = (
        'id',
        'name',
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
        'name',
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
                    'name',
                    'description'
                )
            }
        ),
        (
            'Relations', {
                'fields': (
                    'owner',
                    'routes'
                )
            }
        ),
        (
            'Publication', {
                'fields': (
                    'is_public',
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


@admin.register(SectionModel)
class SectionAdmin(admin.ModelAdmin):
    """
    Admin panel for managing SectionModel objects.
    """

    model = SectionModel
    list_display = (
        'id',
        'name',
        'route',
        'order',
        'distance',
        'created',
        'updated'
    )
    list_filter = (
        'route',
        'created',
        'updated'
    )
    search_fields = (
        'name',
        'description',
        'route__name'
    )
    ordering = (
        'order',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    'description',
                    'order'
                )
            }
        ),
        (
            'Relations', {
                'fields': (
                    'route',
                )
            }
        ),
        (
            'Section data', {
                'fields': (
                    'distance',
                    'ascent',
                    'descent',
                    'duration'
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
