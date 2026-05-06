from django.contrib import admin
from .models import Delivery, DeliveryDetail

class DeliveryDetailInline(admin.TabularInline):
    model = DeliveryDetail
    extra = 1

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('code', 'request', 'user', 'status', 'delivery_at', 'created')
    list_filter = ('status',)
    search_fields = ('code', 'request__code')
    inlines = [DeliveryDetailInline]
