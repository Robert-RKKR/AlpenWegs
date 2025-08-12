# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter

# AlpenWegs application import:
from profiles.models.user_model import UserModel


# User Model filter class:
class UserFilter(BaseFilter):

    class Meta:

        model = UserModel
        fields = {
            # Timestamp Filters:
            'created': ['exact', 'icontains', 'lt', 'gt'],
            'updated': ['exact', 'icontains', 'lt', 'gt'],
            # Django User Filters:
            'is_staff': ['exact'],
            'is_superuser': ['exact'],
            # User Identification Filters:
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'middle_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            # User Password Filters:
            'password_to_change': ['exact'],
            # User Personal Information Filters:
            'gender': ['exact', 'icontains'],
            'weight': ['exact', 'icontains'],
            'height': ['exact', 'icontains'],
            'bmi': ['exact', 'icontains'],
            'birthday': ['exact', 'icontains'],
            # User Location Information Filters:
            'location': ['exact', 'icontains'],
            'location_name': ['exact', 'icontains'],
        }
