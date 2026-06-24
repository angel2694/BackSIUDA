from django.contrib import admin
from .models import Proforma, Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'name', 'contact_name', 'phone', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('ruc', 'name', 'contact_name')

@admin.register(Proforma)
class ProformaAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'date', 'status', 'created', 'updated')
    list_filter = ('status',)
    search_fields = ('supplier__name', 'date')

