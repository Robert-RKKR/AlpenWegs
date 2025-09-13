# Django import:
from django.contrib import admin

# AlpenWegs import:
from explorers.models.route_model import RouteModel
from explorers.models.trip_model import TripModel
from explorers.models.section_model import SectionModel
from explorers.models.section_model import (
    SectionToPhotoModel,
    SectionToPoiModel,
    SectionToCardModel,
    SectionToRegionModel,
)

@admin.register(RouteModel)
class RouteAdmin(admin.ModelAdmin):
    """
    Admin panel for managing RouteModel objects.
    """

    model = RouteModel
    list_display = (
        'id',
        'name',
        'difficulty',
        'created',
        'updated',
    )
    list_filter = (
        'difficulty',
        'created',
        'updated',
    )
    search_fields = (
        'name',
        'description',
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
                    'description',
                    'category',
                    'category_specific_difficulty',
                )
            }
        ),
        (
            'Route data', {
                'fields': (
                    'difficulty',
                    'stamina_requirement',
                    'experience_requirement',
                    'potential_risk_requirement',
                    'potential_risk_description',
                    'family_friendly',
                    'best_seasons',
                    'best_months',
                    'winter_season',
                    'summer_season',
                )
            }
        ),
        (
            'Relations', {
                'fields': (
                    'gpx_file',
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

    readonly_fields = (
        'created',
        'updated'
    )


@admin.register(TripModel)
class TripAdmin(admin.ModelAdmin):
    """
    Admin panel for managing TripModel objects.
    """

    model = TripModel
    list_display = (
        'id',
        'name',
        'creator',
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
        'creator__email',
        'creator__first_name',
        'creator__last_name'
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
                    'creator',
                    'description',
                    'trips',
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

    readonly_fields = (
        'created',
        'updated'
    )


class SectionToPhotoInline(admin.TabularInline):
    model = SectionToPhotoModel
    extra = 1


class SectionToPoiInline(admin.TabularInline):
    model = SectionToPoiModel
    extra = 1


class SectionToCardInline(admin.TabularInline):
    model = SectionToCardModel
    extra = 1


class SectionToRegionInline(admin.TabularInline):
    model = SectionToRegionModel
    extra = 1


@admin.register(SectionModel)
class SectionAdmin(admin.ModelAdmin):
    """
    Admin panel for managing SectionModel objects.
    """

    model = SectionModel
    list_display = (
        'id',
        'name',
        'distance',
        'created',
        'updated',
    )
    list_filter = (
        'created',
        'updated',
    )
    search_fields = (
        'name',
        'description',
        'route__name',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    'snippet',
                    'creator',
                    'description',
                )
            }
        ),
        (
            'GPX', {
                'fields': (
                    'duration',
                    'distance',
                    'elevation_gain',
                    'elevation_loss',
                    'highest_elevation',
                    'lowest_elevation',
                    'average_grade',
                    'highest_grade',
                    'track_types',
                )
            }
        ),
        (
            'Route data', {
                'fields': (
                    'difficulty',
                    'stamina_requirement',
                    'experience_requirement',
                    'potential_risk_requirement',
                    'potential_risk_description',
                    'family_friendly',
                    'best_seasons',
                    'best_months',
                    'winter_season',
                    'summer_season',
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

    readonly_fields = (
        'created',
        'updated'
    )

    inlines = [
        SectionToPhotoInline,
        SectionToPoiInline,
        SectionToCardInline,
        SectionToRegionInline,
    ]
