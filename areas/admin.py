from django.contrib import admin
from .models import Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
