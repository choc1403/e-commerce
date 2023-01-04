from django.contrib import admin
from .models import VotoProducto, VotoComentario, VotoRespuesta
# Register your models here.

admin.site.register(VotoProducto)
admin.site.register(VotoComentario)
admin.site.register(VotoRespuesta)