# AlpenWegs application import:
from assets.models.photo_model import PhotoModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter


# Photo Model filter class:
class PhotoFilter(
    BaseFilter,
):

    class Meta:

        #
        model = PhotoModel
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
            'path': ['exact', 'icontains'],
            'format': ['exact', 'icontains'],
        }
