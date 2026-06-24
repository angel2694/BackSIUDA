import re
from datetime import date
from rest_framework import serializers
from .models import Supplier, Proforma, ProformaItem

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

    def validate_ruc(self, value):
        ruc = value.strip() if value else ''
        if not ruc:
            raise serializers.ValidationError('El RUC es obligatorio.')
        if not ruc.isdigit():
            raise serializers.ValidationError('El RUC solo debe contener dígitos.')
        if len(ruc) != 11:
            raise serializers.ValidationError('El RUC debe tener exactamente 11 dígitos.')
        return ruc

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('El nombre del proveedor es obligatorio.')
        if len(value.strip()) < 3:
            raise serializers.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return value.strip()

    def validate_email(self, value):
        if value and value.strip():
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
            if not re.match(pattern, value.strip()):
                raise serializers.ValidationError('El formato del correo electrónico no es válido.')
        return value.strip() if value else value

    def validate_phone(self, value):
        if value and value.strip():
            phone = value.strip().replace(' ', '').replace('-', '')
            if not phone.isdigit():
                raise serializers.ValidationError('El teléfono solo debe contener dígitos.')
            if len(phone) < 7 or len(phone) > 15:
                raise serializers.ValidationError('El teléfono debe tener entre 7 y 15 dígitos.')
        return value.strip() if value else value


class ProformaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProformaItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'total']
        read_only_fields = ['total']

    def validate_quantity(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError('La cantidad debe ser mayor a 0.')
        return value

    def validate_unit_price(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError('El precio unitario debe ser mayor a 0.')
        return value


class ProformaSerializer(serializers.ModelSerializer):
    items = ProformaItemSerializer(many=True)

    class Meta:
        model = Proforma
        fields = '__all__'

    def validate_date(self, value):
        if value.year < 2000:
            raise serializers.ValidationError('La fecha no puede ser anterior al año 2000.')
        if value > date(2100, 12, 31):
            raise serializers.ValidationError('La fecha ingresada no es válida.')
        return value

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError('La proforma debe tener al menos un ítem.')
        return value

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        proforma = Proforma.objects.create(**validated_data)
        for item in items_data:
            ProformaItem.objects.create(proforma=proforma, **item)
        return proforma
