from django.db import models

class Request(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('APPROVED', 'Aprobada'),
        ('REJECTED', 'Rechazada'),
        ('ATTENDED', 'Atendido'),
    ]
    code = models.CharField(max_length=20, unique=True, verbose_name='Código')
    area = models.ForeignKey('areas.Area', on_delete=models.CASCADE, verbose_name='Área')
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, verbose_name='Usuario')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING', verbose_name='Estado')
    notes = models.TextField(blank=True, verbose_name='Notas')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.code}"

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'

class RequestDetail(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='details', verbose_name='Solicitud')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE, verbose_name='Producto')
    quantity_requested = models.IntegerField(verbose_name='Cantidad Solicitada')
    quantity_attended = models.IntegerField(default=0, verbose_name='Cantidad Atendida')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.request.code} "

    class Meta:
        verbose_name = 'Detalle de solicitud'
        verbose_name_plural = 'Detalles'
