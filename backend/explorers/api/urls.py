# AlpenWegs import:
from alpenwegs.ashared.api.base_default_router import BaseDefaultRouter

# AlpenWegs application import:
from explorers.api.views.route_view import RouteView
from explorers.api.views.trip_view import TripView
from explorers.api.views.section_view import SectionView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-explorers'

# Standard view route registration:
router.register(r'route', RouteView, basename='route_model')
router.register(r'trip', TripView, basename='trip_model')
router.register(r'section', SectionView, basename='section_model')

# Add urlpatterns:
urlpatterns = router.urls
