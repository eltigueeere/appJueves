from django.db.models import Sum
from django.db import models

class  PedidoEnTienda(models.Model):
    usuario  = models.CharField(blank=True, null=True, max_length=99)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaDeOrden  = models.DateTimeField(blank=True, null=True)
    pedido = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        ordering = ['fechaDeOrden']