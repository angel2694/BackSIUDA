from .views import AreaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AreaViewSet, basename='area')
urlpatterns = router.urls