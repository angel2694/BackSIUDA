from django.db import models

# Create your models here.
class Supplier(models.Model):
    ruc = models.CharField(max_length=20, unique=True, verbose_name='RUC')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    contact_name = models.CharField(max_length=100, blank=True, verbose_name='Contacto')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    email = models.EmailField(blank=True, verbose_name='Correo Electrónico')
    address = models.TextField(blank=True, verbose_name='Dirección')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
