# AlpenWegs import:
from alpenwegs.ashared.api.base_default_router import BaseDefaultRouter

# AlpenWegs application import:
from assets.api.views.photo_view import PhotoView
from assets.api.views.file_view import FileView

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-assets'

# Standard view route registration:
router.register(r'photo', PhotoView, basename='photo_model')
router.register(r'file', FileView, basename='file_model')

# Add urlpatterns:
urlpatterns = router.urls
