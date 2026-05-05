from django.contrib import admin

# Register your models here.
from .models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    list_filter = ('role','is_active')
    search_fields = ('username', 'email')
