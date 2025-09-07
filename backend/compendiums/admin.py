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
        'category',
        'created',
        'updated',
    )
    list_filter = (
        'region',
        'created',
        'updated'
    )
    search_fields = (
        'name',
        'snippet',
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
                    'snippet',
                    'category',
                    'creator',
                )
            }
        ),
        (
            'Description', {
                'fields': (
                    'description',
                    'elevation',
                )
            }
        ),
        (
            'Region', {
                'fields': (
                    'region',
                )
            }
        ),
        (
            'Metadata', {
                'fields': (
                    'created',
                    'updated',
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
        'name',
        'category',
        'created',
        'updated',
    )
    list_filter = (
        'category',
        'created',
        'updated',
    )
    search_fields = (
        'name',
        'snippet',
        'region__name',
    )
    ordering = (
        '-created',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    'snippet',
                    'category',
                    'category_specific_difficulty',
                    'creator',
                )
            }
        ),
        (
            'Description', {
                'fields': (
                    'description',
                    'elevation',
                )
            }
        ),
        (
            'PoI', {
                'fields': (
                    'poi',
                )
            }
        ),
        (
            'Metadata', {
                'fields': (
                    'created',
                    'updated',
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
        'created',
        'updated',
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
                    'snippet',
                    'creator',
                )
            }
        ),
        (
            'Description', {
                'fields': (
                    'description',
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
