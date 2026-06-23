from rest_framework.routers import DefaultRouter
from .views import ProformaViewSet

router = DefaultRouter()
router.register(r'', ProformaViewSet, basename='proforma')
urlpatterns = router.urls