from rest_framework.viewsets import ModelViewSet
from accounts.permissions import IsAdminOrReadOnly
from .models import Area
from .serializers import AreaSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin
class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all().order_by('id')
    serializer_class = AreaSerializer
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [IsAuthenticated, IsAdmin]