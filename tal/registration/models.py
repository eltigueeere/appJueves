from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    nombre = models.CharField(max_length=99,null=True, blank=True)
    apellido = models.CharField(max_length=99, null=True, blank=True)
    birthday = models.CharField(max_length=13, null=True, blank=True)
    telefono = models.CharField(max_length=99, null=True, blank=True)
    calle = models.CharField(max_length=99, null=True, blank=True)
    numero = models.CharField(max_length=99, null=True, blank=True)
    colonia = models.CharField(max_length=99, null=True, blank=True)
    cp =  models.CharField(max_length=99, null=True, blank=True)
    esEmpresa = models.BooleanField( null=True, blank=True)
    nombreEmpresa = models.CharField(max_length=99, null=True, blank=True)


    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("Se acaba de crear un usuario y su perfil enlazado")