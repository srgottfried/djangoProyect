from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    imagen = models.ImageField(null=True,
                               upload_to='base/static/img/upload/',
                               default='base/static/img/default/',
                               blank=True)
    apto_para = models.TextField(blank=True)
    alergenos = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nombre}'


class Servicio(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=5, null=False)
    imagen = models.ImageField(null=True,
                               upload_to='base/static/img/upload/',
                               default='base/static/img/default/',
                               blank=True)

    def __str__(self):
        return f'{self.nombre}'


class Pedido(models.Model):
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(null=True,
                                   blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    productos = models.ManyToManyField(Producto,
                                       related_name='productos',
                                       blank=True)
    servicios = models.ManyToManyField(Servicio,
                                       related_name='servicios',
                                       blank=True)
    direccion = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo']
