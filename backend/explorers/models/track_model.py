# AlpenWegs import:
from alpenwegs.ashared.models.identification_model import BaseIdentificationModel
from alpenwegs.ashared.models.sport_category_model import BaseSportCategoryModel
from alpenwegs.ashared.models.accomplished_model import BaseAccomplishedModel
from alpenwegs.ashared.models.descriptive_model import BaseDescriptiveModel
from alpenwegs.ashared.models.statistic_model import BaseStatisticModel
from alpenwegs.ashared.models.timestamp_model import BaseTimestampModel
from alpenwegs.ashared.models.gpx_track_model import BaseGpxTrackModel
from alpenwegs.ashared.models.creator_model import BaseCreatorModel
from alpenwegs.ashared.models.liked_model import BaseLikedModel
from alpenwegs.ashared.models.score_model import BaseScoreModel
from alpenwegs.ashared.models.gpx_model import BaseGpxModel

# AlpenWegs application import:
from explorers.models.journey_model import JourneyModel

# Django import:
from django.db import models


# Track Model class:
class TrackModel(
    BaseIdentificationModel,
    BaseSportCategoryModel,
    BaseAccomplishedModel,
    BaseDescriptiveModel,
    BaseTimestampModel,
    BaseStatisticModel,
    BaseGpxTrackModel,
    BaseCreatorModel,
    BaseLikedModel,
    BaseScoreModel,
    BaseGpxModel,
):
    """
    Model representing a single recorded Track (user activity).
    """

    class Meta:

        # Model name values:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

        # Add custom AlpenWegs permissions:
        permissions = [
            ('change_own_trackmodel', 'Can change own tracks'),
            ('change_all_trackmodel', 'Can change all tracks'),
            ('delete_own_trackmodel', 'Can delete own tracks'),
            ('delete_all_trackmodel', 'Can delete all tracks'),
            ('view_own_trackmodel', 'Can view own tracks'),
            ('view_all_trackmodel', 'Can view all tracks'),
            ('add_own_trackmodel', 'Can add own tracks'),
        ]

    # Default roles and their permissions:
    ROLE_PERMS = {
        'Member': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own',
        ],
        'Author': [
            'change_own',
            'delete_own',
            'view_own',
            'add_own',
        ],
        'Admin': [
            'change_all',
            'change_own',
            'delete_all',
            'delete_own',
            'view_all',
            'view_own',
            'add_own',
        ],
    }

    # Track Many-to-Many Relationships (reverse side):
    journey = models.ForeignKey(
        JourneyModel,
        verbose_name='Related Journey',
        help_text=(
            'Optional Journey that this Track is part of. This allows grouping '
            'multiple Tracks into a larger objective, such as a multi-day hike '
            'or trek. A Journey provides a structured context for activities '
            'that span several days, routes, or regions.'
        ),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # Track analysis metadata:
    verified = models.BooleanField(
        verbose_name='Verified Track',
        help_text=(
            'Indicates that this Track has been formally verified by AlpenWegs. '
            'Verification includes automated geometric comparison between the '
            'user-recorded GPS data and the official Route or Section. The '
            'system evaluates point alignment, elevation profile accuracy, '
            'detour detection, and path overlap to confirm fidelity '
            'to the intended trail.'
        ),
        default=False,
    )
    similarity_index = models.FloatField(
        verbose_name='Similarity Index (%)',
        help_text=(
            'Quantitative score (0-100%) representing how closely this recorded '
            'activity follows the corresponding official trail. The value '
            'incorporates spatial alignment, elevation-profile matching, '
            'route coverage, and deviation distance. Higher values indicate '
            'strong adherence to the mapped trail, while lower values may '
            'reflect detours, GPS drift, or intentional exploration.'
        ),
        blank=True,
        null=True,
    )

    # Track user metadata:
    user_notes = models.TextField(
        verbose_name='User Notes',
        help_text=(
            'Optional textual notes provided by the user, capturing personal '
            'observations (such as weather, terrain, equipment, hazards, or '
            'group behaviour) that are not detectable from GPS data alone. '
            'Useful for retrospective insight and contextual interpretation '
            'of performance or conditions.'
        ),
        blank=True,
        null=True,
    )

    # Track environment metadata:
    snow_track = models.BooleanField(
        verbose_name='Snow Track',
        help_text=(
            'Indicates that this activity occurred in snowy terrain, including '
            'deep snow, packed snow, icy surfaces, or winter conditions. Snow '
            'can affect traction, route visibility, GPS accuracy, '
            'and physical effort.'
        ),
        default=False,
    )
    night_track = models.BooleanField(
        verbose_name='Night Track',
        help_text=(
            'Indicates that significant portions of the Track were completed '
            'during nighttime or in low-visibility conditions. Night tracks '
            'often require additional equipment (headlamps), slower pace, '
            'and increased navigation care.'
        ),
        default=False,
    )
    fog_track = models.BooleanField(
        verbose_name='Fog / Low Visibility',
        help_text=(
            'Marks that the activity was performed in fog, mist, or other '
            'low-visibility conditions. This may have affected navigation '
            'precision, pace, and route selection. Often correlates with '
            'lower similarity-index results.'
        ),
        default=False,
    )
    rain_track = models.BooleanField(
        verbose_name='Rainy Conditions',
        help_text=(
            'Indicates that the activity occurred during rainfall or '
            'wet-weather conditions. Rain influences trail difficulty, '
            'ground stability, and can increase the risk of slipping '
            'or equipment malfunction.'
        ),
        default=False,
    )
    hot_weather_track = models.BooleanField(
        verbose_name='Hot Weather',
        help_text=(
            'Marks that the activity took place in abnormally hot or humid '
            'conditions. High temperatures may affect hydration, heart rate, '
            'fatigue, and overall performance. Important for interpreting '
            'longer rest intervals or reduced pace.'
        ),
        default=False,
    )
    cold_weather_track = models.BooleanField(
        verbose_name='Cold Weather',
        help_text=(
            'Indicates that the activity was performed in cold or freezing '
            'conditions. Cold weather affects user physiology, equipment '
            'performance, and GPS battery consumption. It often correlates '
            'with slower pace and increased energy demand.'
        ),
        default=False,
    )
    windy_track = models.BooleanField(
        verbose_name='Windy Conditions',
        help_text=(
            'Indicates that the activity took place under strong or '
            'destabilising wind conditions. Wind can influence balance, '
            'comfort, safety on exposed ridges, and perceived temperature.'
        ),
        default=False,
    )

    # Track social & group activity metadata:
    group_track = models.BooleanField(
        verbose_name='Group Track',
        help_text=(
            'Indicates participation in a group activity with multiple '
            'individuals. Group dynamics often influence pace, break '
            'frequency, risk decisions, and route selection.'
        ),
        default=False,
    )
    organized_track = models.BooleanField(
        verbose_name='Organized Group Event',
        help_text=(
            'Marks that the Track was part of a structured, organized event '
            'such as a club outing, Meetup event, professionally guided tour, '
            'or scheduled group hike. Distinguishes coordinated events '
            'from informal gatherings.'
        ),
        default=False,
    )
    leader_track = models.BooleanField(
        verbose_name='User Was Group Leader',
        help_text=(
            'Indicates that the user acted as the main organizer or leader '
            'of the group. Responsibilities typically include navigation, pace '
            'regulation, group safety, risk assessment, emergency decision-'
            'making, and ensuring participant readiness. Useful for tracking '
            'leadership experience.'
        ),
        default=False,
    )
    guided_tour_track = models.BooleanField(
        verbose_name='Guided Tour',
        help_text=(
            'Indicates participation in a professionally guided tour, often '
            'involving specialized instruction, mountain-guide supervision, '
            'or technical coaching.'
        ),
        default=False,
    )

    # Track activity style metadata:
    backpacking_track = models.BooleanField(
        verbose_name='Backpacking Track',
        help_text=(
            'Indicates that the user carried substantial gear (sleeping '
            'equipment, cooking gear, multi-day supplies) for extended '
            'travel. Backpacking typically reduces pace due to increased '
            'physical load and affects fatigue accumulation.'
        ),
        default=False,
    )
    fast_hike_track = models.BooleanField(
        verbose_name='Fast Hiking / Speed Activity',
        help_text=(
            'Marks the Track as a high-intensity, performance-focused activity '
            'such as speed hiking or fast trekking. Usually associated with '
            'limited breaks and intentional time optimization.'
        ),
        default=False,
    )
    training_track = models.BooleanField(
        verbose_name='Training Session',
        help_text=(
            'Indicates that the activity was part of structured training rather '
            'than recreational hiking. This includes endurance conditioning, '
            'interval practice, hill repeats, cardiovascular training, or '
            'specific athletic preparation.'
        ),
        default=False,
    )
    exploration_track = models.BooleanField(
        verbose_name='Exploration / Off-Route Activity',
        help_text=(
            'Marks activities that intentionally deviated from official or '
            'marked trails. Exploration may involve off-route travel, '
            'bushwhacking, unmapped paths, or investigation of alternative '
            'terrain. Helpful when explaining deviations from expected '
            'trail geometry.'
        ),
        default=False,
    )

    # Track safety metadata.
    hazardous_track = models.BooleanField(
        verbose_name='Hazardous Conditions',
        help_text=(
            'Indicates that the activity involved environmental or terrain '
            'hazards such as steep icy slopes, scree, avalanche exposure, '
            'rockfall, unstable ground, or dangerous weather. This tag '
            'highlights elevated risk and safety relevance.'
        ),
        default=False,
    )
    injury_occurred = models.BooleanField(
        verbose_name='Injury Occurred',
        help_text=(
            'Indicates that the user or a group member experienced an injury, '
            'ranging from minor sprains to more significant incidents. Useful '
            'for retrospective analysis and identifying safety patterns.'
        ),
        default=False,
    )
    rescue_assistance = models.BooleanField(
        verbose_name='Rescue / Assistance Required',
        help_text=(
            'Indicates that external help was required during the activity, '
            'such as calling mountain rescue, requiring helicopter evacuation, '
            'or receiving emergency or first-aid support. Important for '
            'understanding severe incidents and their context.'
        ),
        default=False,
    )
