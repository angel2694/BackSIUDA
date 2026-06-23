from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer
from accounts.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]  # Permitir acceso solo a usuarios autenticados y administradores
