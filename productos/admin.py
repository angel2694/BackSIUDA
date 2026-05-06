from django.contrib import admin
from .models import Category, UnitMeasure, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    readonly_fields = ('created', 'updated')

@admin.register(UnitMeasure)
class UnitMeasureAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'category', 'min_stock', 'is_active')
    list_filter = ('is_active', 'category')
    search_fields = ('code', 'name')
