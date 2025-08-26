# AlpenWegs import:
from alpenwegs.ashared.api.base_default_router import BaseDefaultRouter

# AlpenWegs application import:
from profiles.api.views.user_view import UserView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-report'

# Report view route registration:
router.register(r'user', UserView, basename='user')

# Add urlpatterns:
urlpatterns = router.urls
