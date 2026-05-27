from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Modulo, RolModulo

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Rol', {'fields': ('role',)}),
    )

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'url', 'icono', 'activo')
    list_editable = ('activo',)

@admin.register(RolModulo)
class RolModuloAdmin(admin.ModelAdmin):
    list_display = ('rol', 'modulo', 'activo')
    list_filter = ('rol', 'activo')
    list_editable = ('activo',)