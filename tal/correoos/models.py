from django.db import models

# Create your models here.

class CorreosCumpleInvitacionPublicidad(models.Model):
    usuarioEmpresa = models.CharField(blank=True, max_length=255)
    esCumple = models.CharField(blank=True, max_length=13)
    invitacion = models.CharField(blank=True, max_length=13)


    class Meta:
        ordering=['usuarioEmpresa']
