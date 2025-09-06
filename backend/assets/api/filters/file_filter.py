# AlpenWegs application import:
from assets.models.file_model import FileModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# File Model filter class:
class FileFilter(
    BaseFilter,
):

    class Meta:

        model = FileModel
        fields = {
            # BaseModel values:
            'id': ['exact'],

            # BaseIdentificationModel values:
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'snippet': ['exact', 'icontains'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseTimestampModel values:
            'created': ['exact', 'lt', 'gt'],
            'updated': ['exact', 'lt', 'gt'],

            # FileModel values:
            'file': ['exact', 'icontains'],
            'format': ['exact', 'icontains'],
        }
