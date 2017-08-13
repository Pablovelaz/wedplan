from django.db import models
from modules.tareas.models import Tarea
from modules.user.models import User
import datetime

# Create your models here.
def user_directory_path(instance,filename):
    #Va subir la imagene en el media root de cada usuario
    return 'user_{0}/{1}'.format(instance.usuario.id,filename)

class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    orden = models.CharField(max_length=500)
    num_inv = models.IntegerField()
    fecha = models.DateTimeField(auto_now=True)
    lugar = models.CharField(max_length=300)
    croquis = models.ImageField(upload_to = user_directory_path)
    tar = models.ManyToManyField(Tarea, related_name='tareas')
    user = models.ForeignKey(User, related_name='usuario')

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "Evento %s" % (self.nombre)
