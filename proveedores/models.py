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

class Proforma(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Proveedor')
    date = models.DateField(verbose_name='Fecha')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente', verbose_name='Estado')
    notes = models.TextField(blank=True, verbose_name='Notas')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"Proforma #{self.id} - {self.supplier}"

    class Meta:
        verbose_name = 'Proforma'
        verbose_name_plural = 'Proformas'

class ProformaItem(models.Model):
    proforma = models.ForeignKey(Proforma, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.IntegerField(verbose_name='Cantidad')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio unitario')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total')

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ítem de proforma'
        verbose_name_plural = 'Ítems de proforma'