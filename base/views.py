from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Pedido, Servicio
from .models import Producto


def index(request):
    return render(request, 'base/index.html')


def sobre_nosotros(request):
    return render(request, 'base/sobre_nosotros.html')


def contacto(request):
    return render(request, 'base/contacto.html')


def proveedores(request):
    return render(request, 'base/proveedores.html')


class Logueo(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pedidos')


class PaginaRegistro(FormView):
    template_name = "base/registro.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pedidos')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pedidos')
        return super(PaginaRegistro, self).get(*args, **kwargs)


class ListaPedidos(LoginRequiredMixin, ListView):
    model = Pedido
    context_object_name = 'pedidos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedidos'] = context['pedidos'].filter(usuario=self.request.user)
        context['count'] = context['pedidos'].filter(completo=False).count()

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['pedidos'] = context['pedidos'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context


class DetallePedido(LoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'base/pedido.html'


class CrearPedido(LoginRequiredMixin, CreateView):
    model = Pedido
    fields = ['titulo', 'descripcion', 'completo', 'productos', 'servicios', 'direccion']
    success_url = reverse_lazy('pedidos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearPedido, self).form_valid(form)


class EditarPedido(LoginRequiredMixin, UpdateView):
    model = Pedido
    fields = ['titulo', 'descripcion', 'completo', 'productos', 'servicios', 'direccion']
    success_url = reverse_lazy('pedidos')


class EliminarPedido(LoginRequiredMixin, DeleteView):
    model = Pedido
    context_object_name = 'pedido'
    success_url = reverse_lazy('pedidos')


class ListaProductos(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = "base/productos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['productos'] = context['productos'].filter(nombre__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context


class ListaServicios(ListView):
    model = Servicio
    context_object_name = 'servicios'
    template_name = "base/servicios.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['servicios'] = context['servicios'].filter(nombre__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context
