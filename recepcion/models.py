from django.db import models

# Create your models here.
class Reception(models.Model):
    order = models.ForeignKey('ordenes.PurchaseOrder', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    received_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=[('COMPLETED', 'Completada'),('INCOMPLETE', 'Incompleta'),('INCIDENT', 'Con incidencia')], default='INCOMPLETE')
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.order.code} - {self.user.username} - {self.received_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
class ReceptionDetail(models.Model):
    reception = models.ForeignKey(Reception, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE)
    quantity_expected = models.IntegerField()
    quantity_received = models.IntegerField(default=0)
    has_incident = models.BooleanField(default=False)
    incident_notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reception.order.code} - {self.quantity_received} - {self.product.unit_measure.name}"