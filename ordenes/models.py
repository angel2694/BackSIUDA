from django.db import models

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Borrador'),
        ('APPROVED', 'Aprobada'),
        ('SENT', 'Enviada'),
        ('RECEIVED', 'Recibida'),
        ('CANCELLED', 'Cancelada'),
    ]
    code = models.CharField(max_length=20, unique=True, verbose_name='Código')
    supplier = models.ForeignKey('proveedores.Supplier', on_delete=models.CASCADE, verbose_name='Proveedor')
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, verbose_name='Usuario')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='DRAFT', verbose_name='Estado')
    notes = models.TextField(blank=True, verbose_name='Notas')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        # return f"{self.code} - {self.supplier.name} - {self.get_status_display()}"
        return f"{self.code}"

    class Meta:
        verbose_name = 'Orden de compra'
        verbose_name_plural = 'Órdenes de compra'

class PurchaseOrderDetail(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='details', verbose_name='Orden')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.IntegerField(verbose_name='Cantidad')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Unitario')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.order.code}"

    class Meta:
        verbose_name = 'Detalle de orden'
        verbose_name_plural = 'Detalles de orden'
