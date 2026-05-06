from django.contrib import admin
from .models import Stock, Movement

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
    search_fields = ('product__name', 'product__code')

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity',  'updated')
    list_filter = ('movement_type',)
    search_fields = ('product__name',)
