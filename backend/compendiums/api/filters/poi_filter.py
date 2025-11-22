# AlpenWegs application import:
from compendiums.models.poi_model import PoiModel

# AlpenWegs import:
from alpenwegs.ashared.filters.base_filter import BaseFilter

# Django import:
from django_filters import rest_framework as filters
from django.contrib.gis.db.models import PointField


# PoI Model filter class:
class PoiFilter(
    BaseFilter,
):

    class Meta:

        model = PoiModel
        fields = {
            # BaseModel values:
            'id': ['exact'],

            # BaseIdentificationModel values:
            'name': ['exact', 'icontains'],
            'slug': ['exact', 'icontains'],
            'snippet': ['exact', 'icontains'],

            # BaseDescriptiveModel values:
            'description': ['exact', 'icontains'],

            # BaseCreatorModel values:
            'creator': ['exact'],
            'is_public': ['exact'],

            # BaseTimestampModel values:
            'created': ['exact', 'lt', 'gt'],
            'updated': ['exact', 'lt', 'gt'],

            # PoI Model values:
            'region': ['exact'],
            'transport_description': ['exact', 'icontains'],
            'category': ['exact'],
            'elevation': ['exact', 'lt', 'gt'],
        }

        filter_overrides = {
            PointField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'exact',
                },
            },
        }
