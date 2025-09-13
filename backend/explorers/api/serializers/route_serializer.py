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
from explorers.models.route_model import RouteModel

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField


# Route Model serializer details:
model = RouteModel
depth = 0

# Route Model serializer fields:
route_fields = [
    'sections',
]

# Route model serializer combined fields:
fields = (
    base_model_fields
    + base_characteristic_fields
    + base_identification_fields
    + base_sport_category_fields
    + base_timestamp_fields
    + base_statistic_fields
    + base_creator_fields
    + base_score_fields
    + route_fields
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


# Route Detailed serializer:
class RouteDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Route model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Route object
    are required.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:route_model-detail',
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
        help_text=RouteModel.creator.field.help_text,
        required=RouteModel.creator.field.null,
        allow_null=RouteModel.creator.field.blank,
    )

    # Other object Many to Many relation schemas:
    sections = SerializedPkRelatedField(
        queryset=SectionModel.objects.all(),
        serializer=SectionRelationSerializer,
        required=False,
        allow_null=True,
        many=True,
    )


# Route Representation serializer:
class RouteRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Route model. Includes only the fields
    necessary for representing a Route object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Route object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-explorers:route_model-detail',
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


# Route relation serializer:
class RouteRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Route model. Includes all fields of
    the Route model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Route model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-explorers:route_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:
        read_only_fields = read_only_fields
        fields = fields
        model = model
        depth = depth
