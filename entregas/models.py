from django.db import models

class Delivery(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('DELIVERED', 'Entregado'),
        ('DISCONTENT', 'Disconforme'),
    ]
    code = models.CharField(max_length=20, unique=True, verbose_name='Código')
    request = models.ForeignKey('solicitudes.Request', on_delete=models.CASCADE, verbose_name='Solicitud')
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, verbose_name='Usuario')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING', verbose_name='Estado')
    delivery_at = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Entrega')
    notes = models.TextField(blank=True, verbose_name='Notas')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.request.code} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'

class DeliveryDetail(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='details', verbose_name='Entrega')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE, verbose_name='Producto')
    quantity_delivered = models.IntegerField(verbose_name='Cantidad Entregada')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.delivery.code}"

    class Meta:
        verbose_name = 'Detalle de entrega'
        verbose_name_plural = 'Detalles de entrega'
