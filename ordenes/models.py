from django.db import models

# Create your models here.
class PurchaseOrder(models.Model):
    code = models.CharField(max_length=20, unique=True)
    supplier = models.ForeignKey('proveedores.Supplier', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=[('DRAFT','Borrador'),('APPROVED', 'Aprobada'),('SENT', 'Enviado'),('RECEIVED', 'Recibida'),('CANCELLED', 'Cancelado')], default='DRAFT')
    created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.supplier.name} - {self.status}"
    
class PurchaseOrderDetail(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order.code} - {self.quantity} - {self.product.unit_measure.name}"