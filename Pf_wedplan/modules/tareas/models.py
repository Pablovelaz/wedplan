from django.db import models
import datetime


class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "SubTarea %s del Tipo %s" % (self.subta,self.nombre)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    coment = models.TextField()

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "Comentario %s en Tarea %s" % (self.coment,self.tarea)

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fcreacion = models.DateTimeField(default=datetime.datetime.now())
    fplaneado = models.DateTimeField()
    fcompletado = models.DateTimeField()
    completado = models.BooleanField(default=False)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return "SubTarea %s para %s" % (self.nombre,self.fplaneado)

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fcreacion = models.DateTimeField(default=datetime.datetime.now())
    fplaneado = models.DateTimeField()
    fcompletado = models.DateTimeField()
    completado = models.BooleanField(default=False)
    sub = models.ManyToManyField(SubTarea,related_name='subtareas')
    coment = models.ManyToManyField(Comentario,related_name='comentarios')

    class Meta:
        ordering = ("fplaneado",)

    def __str__(self):
        return "Tarea %s para %s" % (self.nombre,self.fplaneado)
