import re
from rest_framework import serializers
from .models import Category, UnitMeasure, Product

SOLO_LETRAS = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s\-]+$'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        v = value.strip() if value else ''
        if not v:
            raise serializers.ValidationError('El nombre de la categoría es obligatorio.')
        if len(v) < 2:
            raise serializers.ValidationError('El nombre debe tener al menos 2 caracteres.')
        if len(v) > 100:
            raise serializers.ValidationError('El nombre no puede superar los 100 caracteres.')
        if not re.match(SOLO_LETRAS, v):
            raise serializers.ValidationError('El nombre solo puede contener letras, espacios y guiones.')
        if re.search(r'\s{2,}', v):
            raise serializers.ValidationError('El nombre no puede tener espacios consecutivos.')
        return v

    def validate_description(self, value):
        if value and len(value.strip()) > 500:
            raise serializers.ValidationError('La descripción no puede superar los 500 caracteres.')
        return value.strip() if value else value


class UnitMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMeasure
        fields = '__all__'

    def validate_name(self, value):
        v = value.strip() if value else ''
        if not v:
            raise serializers.ValidationError('El nombre de la unidad es obligatorio.')
        if len(v) < 2:
            raise serializers.ValidationError('El nombre debe tener al menos 2 caracteres.')
        if len(v) > 50:
            raise serializers.ValidationError('El nombre no puede superar los 50 caracteres.')
        if not re.match(SOLO_LETRAS, v):
            raise serializers.ValidationError('El nombre solo puede contener letras, espacios y guiones.')
        if re.search(r'\s{2,}', v):
            raise serializers.ValidationError('El nombre no puede tener espacios consecutivos.')
        return v

    def validate_abbreviation(self, value):
        v = value.strip() if value else ''
        if not v:
            raise serializers.ValidationError('La abreviatura es obligatoria.')
        if len(v) > 10:
            raise serializers.ValidationError('La abreviatura no puede superar 10 caracteres.')
        if not re.match(r'^[a-zA-Z0-9\.\-]+$', v):
            raise serializers.ValidationError('La abreviatura solo puede contener letras, números, puntos y guiones.')
        return v.upper()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_code(self, value):
        v = value.strip() if value else ''
        if not v:
            raise serializers.ValidationError('El código del producto es obligatorio.')
        if len(v) > 50:
            raise serializers.ValidationError('El código no puede superar los 50 caracteres.')
        if not re.match(r'^[a-zA-Z0-9\-\_]+$', v):
            raise serializers.ValidationError('El código solo puede contener letras, números, guiones y guiones bajos.')
        return v.upper()

    def validate_name(self, value):
        v = value.strip() if value else ''
        if not v:
            raise serializers.ValidationError('El nombre del producto es obligatorio.')
        if len(v) < 2:
            raise serializers.ValidationError('El nombre debe tener al menos 2 caracteres.')
        if len(v) > 200:
            raise serializers.ValidationError('El nombre no puede superar los 200 caracteres.')
        if re.search(r'[<>\"\'\\]', v):
            raise serializers.ValidationError('El nombre contiene caracteres no permitidos.')
        if re.search(r'\s{2,}', v):
            raise serializers.ValidationError('El nombre no puede tener espacios consecutivos.')
        return v

    def validate_min_stock(self, value):
        if value is None or value < 0:
            raise serializers.ValidationError('El stock mínimo no puede ser negativo.')
        if value > 999999:
            raise serializers.ValidationError('El stock mínimo ingresado es demasiado alto.')
        return value
