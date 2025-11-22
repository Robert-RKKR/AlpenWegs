# Django import:
from django.contrib import admin

# AlpenWegs import:
from explorers.models.section_model import SectionModel
from explorers.models.journey_model import JourneyModel
from explorers.models.route_model import RouteModel
from explorers.models.track_model import TrackModel
from explorers.models.trip_model import TripModel
from explorers.models.section_model import (
    SectionToRegionModel,
    SectionToPhotoModel,
    SectionToPoiModel,
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
                    'gpx_data',
                )
            }
        ),
        (
            'Metadata', {
                'fields': (
                    'snippet',
                    'created',
                    'updated',
                )
            }
        ),
    )

    readonly_fields = (
        'snippet',
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
                    'snippet',
                    'created',
                    'updated'
                )
            }
        ),
    )

    readonly_fields = (
        'snippet',
        'created',
        'updated'
    )


class SectionToPhotoInline(admin.TabularInline):
    model = SectionToPhotoModel
    extra = 1


class SectionToPoiInline(admin.TabularInline):
    model = SectionToPoiModel
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
                    'snippet',
                    'created',
                    'updated',
                )
            }
        ),
    )

    readonly_fields = (
        'snippet',
        'created',
        'updated'
    )

    inlines = [
        SectionToRegionInline,
        SectionToPhotoInline,
        SectionToPoiInline,
    ]


class TrackInline(admin.TabularInline):
    model = TrackModel
    extra = 0
    fields = (
        'name',
        'category',
        'distance',
        'duration',
        'verified',
        'similarity_index',
        'created',
    )
    readonly_fields = (
        'snippet',
        'created',
    )
    show_change_link = True


@admin.register(JourneyModel)
class JourneyAdmin(admin.ModelAdmin):
    """
    Admin panel for managing JourneyModel objects.
    """

    model = JourneyModel

    list_display = (
        'id',
        'name',
        'creator',
        'category',
        'is_public',
        'total_days',
        'created',
        'updated',
    )
    list_filter = (
        'category',
        'is_public',
        'created',
        'updated',
    )
    search_fields = (
        'name',
        'description',
        'creator__email',
        'creator__first_name',
        'creator__last_name',
    )
    ordering = (
        '-created',
    )

    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    'creator',
                    'description',
                )
            }
        ),
        (
            'Classification', {
                'fields': (
                    'category',
                    'users_accomplished',
                    'score',
                    'is_public',
                )
            }
        ),
        (
            'Multi-day structure', {
                'fields': (
                    'total_days',
                    'accommodation_type',
                    'trip',
                )
            }
        ),
        (
            'Statistics', {
                'fields': (
                    'distance',
                    'duration',
                    'elevation_gain',
                    'elevation_loss',
                )
            }
        ),
        (
            'Metadata', {
                'fields': (
                    'snippet',
                    'created',
                    'updated',
                )
            }
        ),
    )

    readonly_fields = (
        'snippet',
        'created',
        'updated'
    )

    inlines = [
        TrackInline,
    ]


@admin.register(TrackModel)
class TrackAdmin(admin.ModelAdmin):
    """
    Admin panel for managing TrackModel objects.
    """

    model = TrackModel

    list_display = (
        'id',
        'name',
        'category',
        'journey',
        'route',
        'distance',
        'duration',
        'verified',
        'similarity_index',
        'created',
        'updated',
    )
    list_filter = (
        'category',
        'verified',
        'snow_track',
        'night_track',
        'rain_track',
        'hot_weather_track',
        'cold_weather_track',
        'group_track',
        'organized_track',
        'guided_tour_track',
        'hazardous_track',
        'created',
        'updated',
    )
    search_fields = (
        'name',
        'description',
        'journey__name',
        'route__name',
        'creator__email',
        'creator__first_name',
        'creator__last_name',
    )
    ordering = (
        '-created',
    )

    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    'creator',
                    'description',
                    'user_notes',
                )
            }
        ),
        (
            'Classification', {
                'fields': (
                    'category',
                    'users_accomplished',
                    'score',
                )
            }
        ),
        (
            'Relationships', {
                'fields': (
                    'journey',
                    'route',
                    'verified',
                    'similarity_index',
                )
            }
        ),
        (
            'GPS Data', {
                'fields': (
                    'gpx_data',
                    'distance',
                    'duration',
                    'elevation_gain',
                    'elevation_loss',
                    'highest_elevation',
                    'lowest_elevation',
                )
            }
        ),
        (
            'Environment Conditions', {
                'fields': (
                    'snow_track',
                    'night_track',
                    'fog_track',
                    'rain_track',
                    'hot_weather_track',
                    'cold_weather_track',
                    'windy_track',
                )
            }
        ),
        (
            'Group Activity', {
                'fields': (
                    'group_track',
                    'organized_track',
                    'leader_track',
                    'guided_tour_track',
                )
            }
        ),
        (
            'Activity Style', {
                'fields': (
                    'backpacking_track',
                    'fast_hike_track',
                    'training_track',
                    'exploration_track',
                )
            }
        ),
        (
            'Safety Metadata', {
                'fields': (
                    'hazardous_track',
                    'injury_occurred',
                    'rescue_assistance',
                )
            }
        ),
        (
            'Metadata', {
                'fields': (
                    'snippet',
                    'created',
                    'updated',
                )
            }
        ),
    )

    readonly_fields = (
        'snippet',
        'created',
        'updated',
        'distance',
        'duration',
        'elevation_gain',
        'elevation_loss',
        'highest_elevation',
        'lowest_elevation',
        'verified',
        'similarity_index',
    )
