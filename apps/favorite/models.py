# Modelos
from xml.parsers.expat import model
from django.db import models
from apps.products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class favorito(models.Model):
    usuario = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto.title