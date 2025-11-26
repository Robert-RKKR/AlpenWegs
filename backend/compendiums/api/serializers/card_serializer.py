# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import (
    WritableNestedSerializer,
    BaseSerializer,
)
from alpenwegs.ashared.api.serializers.base_model_variables import (
    base_identification_read_only_fields,
    base_descriptive_read_only_fields,
    base_timestamp_read_only_fields,
    base_creator_read_only_fields,
    base_model_read_only_fields,
    base_identification_fields,
    base_representation_fields,
    base_descriptive_fields,
    base_timestamp_fields,
    base_creator_fields,
    base_model_fields,
)

# AlpenWegs application import:
from alpenwegs.ashared.constants.sport_category_difficulty import SportCategoryDifficultyChoices
from compendiums.api.serializers.poi_serializer import PoiRelationSerializer
from profiles.api.serializers.user_serializer import UserRelationSerializer
from alpenwegs.ashared.constants.sport_category import SportCategoryChoices
from alpenwegs.ashared.constants.card_type import CardTypeChoices
from compendiums.models.card_model import CardModel

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework import serializers


# Card Model serializer details:
model = CardModel
depth = 0

# Card Model serializer fields:
card_fields = [
    'category_specific_difficulty',
    'category',
    'elevation',
    'type',
    'poi',
]

# Card model serializer combined fields:
fields = (
    base_model_fields
    + base_identification_fields
    + base_descriptive_fields
    + base_timestamp_fields
    + base_creator_fields
    + card_fields
)
read_only_fields = (
    base_model_read_only_fields
    + base_identification_read_only_fields
    + base_descriptive_read_only_fields
    + base_timestamp_read_only_fields
    + base_creator_read_only_fields
)


# Card Detailed serializer:
class CardDetailedSerializer(
    BaseSerializer,
):
    """
    Detailed serializer for the Card model. Includes all fields
    of the model together with serializers for related models.

    Used for standard API actions such as create, list, retrieve,
    update, and delete, whenever complete details of a Card object
    are required.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-compendiums:card_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    # Other object relation schemas:
    creator = UserRelationSerializer(
        help_text=CardModel.creator.field.help_text,
        required=CardModel.creator.field.null,
        allow_null=CardModel.creator.field.blank,
    )
    poi = PoiRelationSerializer(
        help_text=CardModel.poi.field.help_text,
        required=CardModel.poi.field.null,
        allow_null=CardModel.poi.field.blank,
    )

    # Special constance fields:
    category_specific_difficulty = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    # Special constance methods:
    def get_category_specific_difficulty(self, obj):
        # Return metadata dict for country:
        return SportCategoryDifficultyChoices.dict_from_int(
            obj.category_specific_difficulty
        )

    def get_category(self, obj):
        # Return metadata dict for country:
        return SportCategoryChoices.dict_from_int(
            obj.category
        )

    def get_type(self, obj):
        # Return metadata dict for country:
        return CardTypeChoices.dict_from_int(
            obj.type
        )

    class Meta:

        # Define read only fields:
        read_only_fields = read_only_fields

        # Define writable fields:
        fields = fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth


# Card Representation serializer:
class CardRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the Card model. Includes only the fields
    necessary for representing a Card object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a Card object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-compendiums:card_model-detail',
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


# Card relation serializer:
class CardRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the Card model. Includes all fields of
    the Card model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the Card model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-compendiums:card_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    # Special constance fields:
    category_specific_difficulty = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    # Special constance methods:
    def get_category_specific_difficulty(self, obj):
        # Return metadata dict for country:
        return SportCategoryDifficultyChoices.dict_from_int(
            obj.category_specific_difficulty
        )

    def get_category(self, obj):
        # Return metadata dict for country:
        return SportCategoryChoices.dict_from_int(
            obj.category
        )

    def get_type(self, obj):
        # Return metadata dict for country:
        return CardTypeChoices.dict_from_int(
            obj.type
        )

    class Meta:

        # Define read only fields:
        read_only_fields = read_only_fields

        # Define writable fields:
        fields = fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth