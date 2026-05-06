from django.db import models

class Reception(models.Model):
    STATUS_CHOICES = [
        ('COMPLETED', 'Completada'),
        ('INCOMPLETE', 'Incompleta'),
        ('INCIDENT', 'Con incidencia'),
    ]
    order = models.ForeignKey('ordenes.PurchaseOrder', on_delete=models.CASCADE, related_name='receptions', verbose_name='Orden')
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, verbose_name='Usuario')
    received_at = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Recepción')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='INCOMPLETE', verbose_name='Estado')
    notes = models.TextField(blank=True, verbose_name='Notas')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.order.code} - {self.user.username} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Recepción'
        verbose_name_plural = 'Recepciones'

class ReceptionDetail(models.Model):
    reception = models.ForeignKey(Reception, on_delete=models.CASCADE, related_name='details', verbose_name='Recepción')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE, verbose_name='Producto')
    quantity_expected = models.IntegerField(verbose_name='Cantidad Esperada')
    quantity_received = models.IntegerField(default=0, verbose_name='Cantidad Recibida')
    has_incident = models.BooleanField(default=False, verbose_name='Con Incidencia')
    incident_notes = models.TextField(blank=True, verbose_name='Notas de Incidencia')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.reception.order.code}"

    class Meta:
        verbose_name = 'Detalle de recepción'
        verbose_name_plural = 'Detalles de recepción'
