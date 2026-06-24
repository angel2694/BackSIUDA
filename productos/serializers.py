from rest_framework import serializers
from .models import Category, UnitMeasure, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('El nombre de la categoría es obligatorio.')
        if len(value.strip()) < 2:
            raise serializers.ValidationError('El nombre debe tener al menos 2 caracteres.')
        return value.strip()

    def validate_description(self, value):
        return value.strip() if value else value


class UnitMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMeasure
        fields = '__all__'

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('El nombre de la unidad es obligatorio.')
        return value.strip()

    def validate_abbreviation(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('La abreviatura es obligatoria.')
        if len(value.strip()) > 10:
            raise serializers.ValidationError('La abreviatura no puede superar 10 caracteres.')
        return value.strip().upper()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_code(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('El código del producto es obligatorio.')
        return value.strip().upper()

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('El nombre del producto es obligatorio.')
        if len(value.strip()) < 2:
            raise serializers.ValidationError('El nombre debe tener al menos 2 caracteres.')
        return value.strip()

    def validate_min_stock(self, value):
        if value is None or value < 0:
            raise serializers.ValidationError('El stock mínimo no puede ser negativo.')
        return value
