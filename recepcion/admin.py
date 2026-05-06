from django.contrib import admin
from .models import Reception, ReceptionDetail

class ReceptionDetailInline(admin.TabularInline):
    model = ReceptionDetail
    extra = 1

@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'status', 'received_at'    )
    list_filter = ('status',)
    search_fields = ('order__code',)
    inlines = [ReceptionDetailInline]
