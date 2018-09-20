from django.db import models

class Producto(nodels.MODEL)
    codigo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=100, blank=True, null=True)
    cantidad=models.IngtegerField(default=0)
    fecha=models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return '{0}-{1}'.format(self.codigo, self.nombre)
