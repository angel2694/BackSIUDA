from rest_framework.routers import DefaultRouter
from .views import UnitMeasureViewSet

router = DefaultRouter()
router.register(r'', UnitMeasureViewSet, basename='unitmeasure')
urlpatterns = router.urls