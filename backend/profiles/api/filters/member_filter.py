# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter

# AlpenWegs application import:
from profiles.models.member_model import MemberModel


# Member Model filter class:
class MemberFilter(BaseFilter):

    class Meta:

        model = MemberModel
        fields = {
            # Timestamp Filters:
            'created': ['exact', 'icontains', 'lt', 'gt'],
            'updated': ['exact', 'icontains', 'lt', 'gt'],
            # Django User Filters:
            'is_staff': ['exact'],
            'is_superuser': ['exact'],
            # Member Identification Filters:
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'middle_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            # Member Password Filters:
            'password_to_change': ['exact'],
            # Member Personal Information Filters:
            'gender': ['exact', 'icontains'],
            'weight': ['exact', 'icontains'],
            'height': ['exact', 'icontains'],
            'bmi': ['exact', 'icontains'],
            'birthday': ['exact', 'icontains'],
            # Member Location Information Filters:
            'location': ['exact', 'icontains'],
            'location_name': ['exact', 'icontains'],
        }
