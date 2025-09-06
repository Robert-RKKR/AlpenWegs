# AlpenWegs application import:
from notifications.models.change_log_model import ChangeLogModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# ChangeLog Model filter class:
class ChangeLogFilter(
    BaseFilter,
):

    class Meta:

        model = ChangeLogModel
        fields = {
            # Object Representation Model values:
            'app_name': ['exact', 'icontains'],
            'model_name': ['exact', 'icontains'],
            'object_id': ['exact'],
            'object_repr': ['exact', 'icontains'],

            # Model data time information:
            'timestamp': ['exact', 'icontains', 'lt', 'gt'],

            # User information:
            'user': ['exact'],
            
            # Change details:
            'action_type': ['exact'],
        }
