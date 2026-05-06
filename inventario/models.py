from django.db import models

# Create your models here.
class Stock(models.Model):
    product = models.OneToOneField('productos.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} - {self.product.unit_measure.name}"

class Movement(models.Model):
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=10, choices=[('IN', 'Entrada'), ('OUT', 'Salida')])
    quantity = models.IntegerField()
    reason = models.TextField(blank=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movement_type} - {self.product.name} - {self.quantity}"