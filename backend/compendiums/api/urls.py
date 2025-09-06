# AlpenWegs import:
from alpenwegs.ashared.api.base_default_router import BaseDefaultRouter

# AlpenWegs application import:
from compendiums.api.views.card_view import CardView
from compendiums.api.views.poi_view import PoiView
from compendiums.api.views.region_view import RegionView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-compendiums'

# Standard view route registration:
router.register(r'card', CardView, basename='card_model')
router.register(r'poi', PoiView, basename='poi_model')
router.register(r'region', RegionView, basename='region_model')

# Add urlpatterns:
urlpatterns = router.urls
