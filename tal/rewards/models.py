from django.db.models import Sum
from django.db import models


# Create your models here.
class Recompensa(models.Model):
    recompensa = models.IntegerField(max_length=99, null=True, blank=True)
    nombreUsuario = models.CharField(max_length=99, null=True, blank=True)
    nombreEmpresaUsuario = models.CharField(max_length=99, null=True, blank=True)
    producto = models.TextField(max_length=99, null=True, blank=True)
    fechaCompra = models.DateTimeField()
    statusRecompensa = models.BooleanField( null=True, blank=True)


    class Meta:
        ordering = ['fechaCompra']
