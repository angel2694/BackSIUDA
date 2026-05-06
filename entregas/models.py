from django.db import models

# Create your models here.
class Delivery(models.Model):
    code = models.CharField(max_length=20, unique=True)
    request = models.ForeignKey('solicitudes.Request', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=[('PENDING', 'Pendiente'), ('DELIVERED', 'Entregado'),('DISCONTENT', 'Disconforme')], default='PENDING')
    delivery_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.request.code} - {self.user.username} - {self.delivery_at} - {self.status}"
    
class DeliveryDetail(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE)
    quantity_delivered = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.delivery.code} - {self.quantity_delivered} - {self.product.unit_measure.name}"
