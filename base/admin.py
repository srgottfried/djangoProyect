from django.contrib import admin
from .models import Pedido, Producto, Servicio

admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Servicio)
