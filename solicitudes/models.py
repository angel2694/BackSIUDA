from django.db import models

# Create your models here.
class Request(models.Model):
    code = models.CharField(max_length=20, unique=True)
    area = models.ForeignKey('areas.Area', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('PENDING', 'Pendiente'), ('APPROVED', 'Aprobada'), ('REJECTED', 'Rechazada'),('ATTENDED', 'Atendido')], default='PENDING')
    created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.area.name} - {self.status}"

class RequestDetail(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE)
    quantity_requested = models.IntegerField()
    quantity_attended = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request.code} - {self.quantity_requested} - {self.product.unit_measure.name}"