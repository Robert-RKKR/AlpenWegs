from django.contrib import admin

from .models.region_model import RegionModel
from .models.card_model import CardModel
from .models.poi_model import PoiModel

admin.site.register(RegionModel)
admin.site.register(CardModel)
admin.site.register(PoiModel)
