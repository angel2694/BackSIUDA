from rest_framework.viewsets import ModelViewSet
from .models import Supplier, Proforma
from .serializers import SupplierSerializer, ProformaSerializer
from accounts.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all().order_by('id')
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class ProformaViewSet(ModelViewSet):
    queryset = Proforma.objects.all().order_by('-created')
    serializer_class = ProformaSerializer
    permission_classes = [IsAuthenticated, IsAdmin]