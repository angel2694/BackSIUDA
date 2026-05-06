from django.contrib import admin
from .models import PurchaseOrder, PurchaseOrderDetail

class PurchaseOrderDetailInline(admin.TabularInline):
    model = PurchaseOrderDetail
    extra = 1

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'supplier', 'user', 'status', 'created')
    list_filter = ('status',)
    search_fields = ('code', 'supplier__name')
    readonly_fields = ('code', 'created', 'updated')
    inlines = [PurchaseOrderDetailInline]
