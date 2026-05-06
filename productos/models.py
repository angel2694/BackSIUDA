from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class UnitMeasure(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    abbreviation = models.CharField(max_length=10, verbose_name='Abreviatura')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'

class Product(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name='Código')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    unit_measure = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE, verbose_name='Unidad de medida')
    min_stock = models.IntegerField(verbose_name='Stock mínimo')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
