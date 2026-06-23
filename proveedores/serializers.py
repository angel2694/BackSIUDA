from rest_framework import serializers
from .models import Supplier, Proforma, ProformaItem

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProformaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProformaItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'total']
        read_only_fields = ['total']

class ProformaSerializer(serializers.ModelSerializer):
    items = ProformaItemSerializer(many=True)

    class Meta:
        model = Proforma
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        proforma = Proforma.objects.create(**validated_data)
        for item in items_data:
            ProformaItem.objects.create(proforma=proforma, **item)
        return proforma