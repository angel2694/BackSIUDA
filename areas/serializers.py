from rest_framework import serializers
from .models import Area

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('El nombre del área es obligatorio.')
        if len(value.strip()) < 2:
            raise serializers.ValidationError('El nombre debe tener al menos 2 caracteres.')
        return value.strip()

    def validate_description(self, value):
        return value.strip() if value else value
