# AlpenWegs import:
from alpenwegs.ashared.api.serializers.base_serializers import WritableNestedSerializer
from alpenwegs.ashared.api.serializers.base_serializers import BaseSerializer

# Rest framework serializer import:
from rest_framework.serializers import HyperlinkedIdentityField

# AlpenWegs application import:
from profiles.models.user_model import UserModel


# User Model serializer details:
model = UserModel
depth = 0
fields = [
    # Base Model values:
    'pk',
    'url',
    # Timestamp model values:
    'created',
    'updated',
    # Required User fields:
    'is_active',
    'is_staff',
    'last_login',
    'is_superuser',
    # Base User identification information:
    'email',
    'username',
    'first_name',
    'middle_name',
    'last_name',
    # Password information:
    'password_to_change',
    # Contact information:
    'phone_number',
    # Personal information:
    'gender',
    'weight',
    'height',
    'bmi',
    'birthday',
    # Location information:
    'location',
    'location_name',
]
read_only_fields = [
    'pk',
    'url',
]
representation_fields = [
    'url',
    'username',
]


# User Model Detailed serializer class:
class UserDetailedSerializer(BaseSerializer):

    # Object URL definition:
    url = HyperlinkedIdentityField(
        view_name='api-profiles:user_model-detail',
        help_text='URL to provided object.',
        read_only=False
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


# User Representation serializer:
class UserRepresentationSerializer(
    BaseSerializer,
):
    """
    Representation serializer for the User model. Includes only the fields
    necessary for representing a User object in API responses.

    Used for standard API actions such as list and retrieve, whenever
    a simplified representation of a User object is sufficient.
    """

    # Default model URL field with hyperlink to retrieve view:
    url = HyperlinkedIdentityField(
        view_name='api-profiles:user_model-detail',
        help_text='URL to provided object.',
        read_only=True,
    )

    class Meta:

        # Define read only fields:
        read_only_fields = representation_fields

        # Define writable fields:
        fields = representation_fields

        # Define related model:
        model = model

        # Define model depth:
        depth = depth


# User relation serializer:
class UserRelationSerializer(
    WritableNestedSerializer,
):
    """
    Relation serializer for the User model. Includes all fields of
    the User model but represents related objects in a simplified form.

    Intended for use in other model serializers when only the relation
    to the User model is needed, not its full details.
    """

    url = HyperlinkedIdentityField(
        view_name='api-profiles:user_model-detail',
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
