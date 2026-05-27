from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),
        ('almacen', 'Almacen'),
        ('inventario', 'Inventario'),
        ('cliente', 'Cliente'),
        ('proveedor', 'Proveedor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    def __str__(self):
        return self.username

class Modulo(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    icono = models.CharField(max_length=50, blank=True, default='')
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nombre


class RolModulo(models.Model):
    rol = models.CharField(max_length=20, choices=CustomUser.ROLE_CHOICES)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='rol_modulos')
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('rol', 'modulo')

    def __str__(self):
        return f'{self.rol} → {self.modulo.nombre}'