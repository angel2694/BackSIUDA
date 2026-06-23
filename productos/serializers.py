from rest_framework import serializers
from .models import Category, UnitMeasure

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UnitMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMeasure
        fields = '__all__'