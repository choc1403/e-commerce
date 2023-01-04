from itertools import product
from django.db import models

from apps.products.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Comentario(models.Model):
    product = models.ForeignKey(Product, blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True,null=False, on_delete=models.CASCADE)
    comentario = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.comentario

class Respuesta(models.Model):
    comentario = models.ForeignKey(Comentario, blank=True, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True,null=False, on_delete=models.CASCADE)
    respuesta = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.respuesta