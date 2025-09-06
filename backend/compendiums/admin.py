# Django import:
from django.contrib import admin

# AlpenWegs import:
from compendiums.models.poi_model import PoiModel
from compendiums.models.card_model import CardModel
from compendiums.models.region_model import RegionModel


@admin.register(PoiModel)
class PoiAdmin(admin.ModelAdmin):
    """
    Admin panel for managing PoiModel objects.
    """

    model = PoiModel
    list_display = (
        'id',
        'name',
        'region',
        'poi_type',
        'latitude',
        'longitude',
        'created',
        'updated'
    )
    list_filter = (
        'poi_type',
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
                    'description',
                    'poi_type'
                )
            }
        ),
        (
            'Location', {
                'fields': (
                    'latitude',
                    'longitude',
                    'region'
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


@admin.register(CardModel)
class CardAdmin(admin.ModelAdmin):
    """
    Admin panel for managing CardModel objects.
    """

    model = CardModel
    list_display = (
        'id',
        'title',
        'region',
        'achievement_type',
        'created',
        'updated'
    )
    list_filter = (
        'achievement_type',
        'region',
        'created',
        'updated'
    )
    search_fields = (
        'title',
        'description',
        'region__name'
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
                    'icon'
                )
            }
        ),
        (
            'Relations', {
                'fields': (
                    'region',
                    'achievement_type'
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


@admin.register(RegionModel)
class RegionAdmin(admin.ModelAdmin):
    """
    Admin panel for managing RegionModel objects.
    """

    model = RegionModel
    list_display = (
        'id',
        'name',
        'country',
        'created',
        'updated'
    )
    list_filter = (
        'country',
        'created',
        'updated'
    )
    search_fields = (
        'name',
        'country__name'
    )
    ordering = (
        'name',
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
                    'country',
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
