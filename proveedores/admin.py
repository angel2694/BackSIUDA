from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'name', 'contact_name', 'phone', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('ruc', 'name', 'contact_name')
