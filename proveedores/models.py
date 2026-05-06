from django.db import models

# Create your models here.
class Supplier(models.Model):
    ruc = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
