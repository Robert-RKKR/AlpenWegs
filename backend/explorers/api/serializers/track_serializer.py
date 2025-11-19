# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    SerializedPkRelatedField,
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_identification_read_only_fields,
    base_sport_category_read_only_fields,
    base_characteristic_read_only_fields,
    base_statistic_read_only_fields,
    base_timestamp_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_score_read_only_fields,
    base_identification_fields,
    base_representation_fields,
    base_characteristic_fields,
    base_sport_category_fields,
    base_statistic_fields,
    base_timestamp_fields,
    base_creator_fields,
    base_model_fields,
    base_score_fields,
)

# AlpenWegs application import:
from explorers.api.serializers.section_serializer import SectionRelationSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from explorers.models.section_model import SectionModel
from explorers.models.track_model import TrackModel

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField


# Track Model serializer details:
model = TrackModel
depth = 0

# Track Model serializer fields:
track_fields = [
    'journey',
    'route',
    'verified',
    'similarity_index',
    'user_notes',
    'snow_track',
    'night_track',
    'fog_track',
    'rain_track',
    'hot_weather_track',
    'cold_weather_track',
    'windy_track',
    'group_track',
    'organized_track',
    'leader_track',
    'guided_tour_track',
    'backpacking_track',
    'fast_hike_track',
    'training_track',
    'exploration_track',
    'hazardous_track',
    'injury_occurred',
    'rescue_assistance',
]

# Track model serializer combined fields:
fields = (
    base_model_fields
    + base_characteristic_fields
    + base_identification_fields
    + base_sport_category_fields
    + base_timestamp_fields
    + base_statistic_fields
    + base_creator_fields
    + base_score_fields
    + track_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_identification_read_only_fields
    + base_characteristic_read_only_fields
    + base_sport_category_read_only_fields
    + base_statistic_read_only_fields
    + base_timestamp_read_only_fields
    + base_creator_read_only_fields
    + base_score_read_only_fields
)


# Track Detailed serializer:
class TrackDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Track model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Track object
    are required.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:track_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth

    # Other object relation schemas:
    creator = UserRelationSerializer(
        help_text=TrackModel.creator.field.help_text,
        required=TrackModel.creator.field.null,
        allow_null=TrackModel.creator.field.blank,
    )

    # Other object Many to Many relation schemas:
    sections = SerializedPkRelatedField(
        queryset=SectionModel.objects.all(),
        serializer=SectionRelationSerializer,
        required=False,
        allow_null=True,
        many=True,
    )


# Track Representation serializer:
class TrackRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Track model. Includes only the fields
    necessary for representing a Track object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Track object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-explorers:track_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:

        # Define read only fields:
        read_only_fields = base_representation_fields

        # Define writable fields:
        fields = base_representation_fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth


# Track relation serializer:
class TrackRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Track model. Includes all fields of
    the Track model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Track model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:track_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth
