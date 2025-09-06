# AlpenWegs import:
from alpenwegs.ashared.api.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.base_serializers import SerializedPkRelatedField
from alpenwegs.ashared.api.base_serializers import BaseSerializer

# Rest framework import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from compendiums.api.serializers.poi_serializer import PoiRelationSerializer
from compendiums.models.card_model import CardModel
from compendiums.models.poi_model import PoiModel


# Card Model serializer details:
model = CardModel
depth = 0
fields = [
    # BaseModel values:
    'pk',
    'url',

    # BaseIdentificationModel values:
    'name',
    'slug',
    'snippet',

    # BaseDescriptiveModel values:
    'description',

    # BaseCreatorModel values:
    'creator',
    'is_public',

    # BaseTimestampModel values:
    'created',
    'updated',

    # CardModel values:
    'poi',
    'elevation',
    'type',
    'category',
    'category_specific_difficulty',
]
read_only_fields = [
    'pk',
    'url',
    'slug',
    'creator',
    'created',
    'updated',
]


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

    # Field related to relations with other models:
    poi = PoiRelationSerializer(
        help_text=PoiModel.region.field.help_text,
        required=PoiModel.region.field.null,
        allow_null=PoiModel.region.field.blank,
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

    class Meta:

        # Define read only fields:
        read_only_fields = read_only_fields

        # Define writable fields:
        fields = fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth