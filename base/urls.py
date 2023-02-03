from django.urls import path
from .views import ListaPedidos, DetallePedido, CrearPedido, EditarPedido, EliminarPedido, Logueo, PaginaRegistro, \
    index, ListaProductos, ListaServicios, sobre_nosotros, contacto, proveedores
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('pedidos/', ListaPedidos.as_view(), name='pedidos'),
    path('login/', Logueo.as_view(), name='login'),
    path('registro/', PaginaRegistro.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('pedido/<int:pk>', DetallePedido.as_view(), name='pedido'),
    path('crear-pedido/', CrearPedido.as_view(), name='crear-pedido'),
    path('editar-pedido/<int:pk>', EditarPedido.as_view(), name='editar-pedido'),
    path('eliminar-pedido/<int:pk>', EliminarPedido.as_view(), name='eliminar-pedido'),
    path('productos/', ListaProductos.as_view(), name='productos'),
    path('servicios/', ListaServicios.as_view(), name='servicios'),
    path('sobre-nosotros/', sobre_nosotros, name='sobre-nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('proveedores/', proveedores, name='proveedores'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
