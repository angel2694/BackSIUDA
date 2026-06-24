from rest_framework.viewsets import ModelViewSet
from .models import Category, UnitMeasure, Product
from .serializers import CategorySerializer, UnitMeasureSerializer, ProductSerializer
from accounts.permissions import IsAdmin, IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class UnitMeasureViewSet(ModelViewSet):
    queryset = UnitMeasure.objects.all().order_by('id')
    serializer_class = UnitMeasureSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]