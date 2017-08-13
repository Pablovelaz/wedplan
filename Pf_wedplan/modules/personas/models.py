from django.db import models
from modules.eventos.models import Eventos

# Create your models here.


class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tel = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True, max_length=100)
    face = models.URLField(unique=True, max_length=500, blank=True, null=True)
    eventos = models.ManyToManyField(Eventos)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "Persona: %s %s" % (self.nombre,self.tipo)


class Servicios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)
    costo_u = models.IntegerField()

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "Servicio: %s. De: %s" % (self.nombre,self.prov)

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tel = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True, max_length=100)
    pagina = models.URLField()
    giro = models.CharField(max_length=100)
    eventos = models.ManyToManyField(Eventos, related_name='eventos')
    serv = models.ManyToManyField(Servicios, related_name='Servicios')

    class Meta:
        ordering = ("giro",)

    def __str__(self):
        return "Proveedor %s de %s" % (self.nombre,self.giro)
