from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin
from .models import Area
from .serializers import AreaSerializer

# Create your views here.
class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all().order_by('id')
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated, IsAdmin]