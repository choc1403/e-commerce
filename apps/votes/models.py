from django.db import models
from apps.products.models import Product
from django.contrib.auth.models import User
from apps.Comments.models import Comentario, Respuesta
# Create your models here.

from django.core.validators import MaxValueValidator, MinValueValidator

class VotoProducto(models.Model):
    user = models.ForeignKey(User, blank=True,null=False, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, blank=True, null=True,on_delete=models.CASCADE)    
    estrellas = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return 'Al producto: ['+self.producto.title+'] Cuantas estrellas tiene: '+str(self.estrellas)


class VotoComentario(models.Model):
    user = models.ForeignKey(User, blank=True,null=False, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, blank=True,null=True, on_delete=models.CASCADE)
    estrellas = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return 'Al comentario: ['+self.comentario.comentario+'] Cuantas estrellas tiene: '+str(self.estrellas)

class VotoRespuesta(models.Model):
    user = models.ForeignKey(User, blank=True,null=False, on_delete=models.CASCADE)    
    respuesta = models.ForeignKey(Respuesta, blank=True,null=True, on_delete=models.CASCADE)
    estrellas = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return 'A la respuesta: ['+self.respuesta.respuesta+'] Cuantas estrellas tiene: '+str(self.estrellas)