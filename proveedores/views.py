from rest_framework.viewsets import ModelViewSet
from .models import Supplier
from .serializers import SupplierSerializer
from accounts.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all().order_by('id')
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsAdmin]