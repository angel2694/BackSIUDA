from django.db import models

class Stock(models.Model):
    product = models.OneToOneField('productos.Product', on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.IntegerField(verbose_name='Cantidad')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.product.name} - {self.quantity} {self.product.unit_measure.abbreviation}"

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'

class Movement(models.Model):
    TYPE_CHOICES = [('IN', 'Entrada'), ('OUT', 'Salida')]

    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE, verbose_name='Producto')
    movement_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Tipo de Movimiento')
    quantity = models.IntegerField(verbose_name='Cantidad')
    reason = models.TextField(blank=True, verbose_name='Motivo')
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, verbose_name='Usuario')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Entrada/Salida')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.product.name} - {self.quantity}"

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos (Kárdex)'
