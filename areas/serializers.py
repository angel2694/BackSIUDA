import re
from rest_framework import serializers
from .models import Area

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

    def validate_name(self, value):
        v = value.strip() if value else ''
        if not v:
            raise serializers.ValidationError('El nombre del área es obligatorio.')
        if len(v) < 2:
            raise serializers.ValidationError('El nombre debe tener al menos 2 caracteres.')
        if len(v) > 100:
            raise serializers.ValidationError('El nombre no puede superar los 100 caracteres.')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s\-]+$', v):
            raise serializers.ValidationError('El nombre solo puede contener letras, espacios y guiones.')
        if re.search(r'\s{2,}', v):
            raise serializers.ValidationError('El nombre no puede tener espacios consecutivos.')
        return v

    def validate_description(self, value):
        if value and len(value.strip()) > 500:
            raise serializers.ValidationError('La descripción no puede superar los 500 caracteres.')
        return value.strip() if value else value
