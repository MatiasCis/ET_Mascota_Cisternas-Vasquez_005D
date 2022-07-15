from re import I
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.decorators import csrf
from .models import *
from .forms import ProductoForm, ClienteForm
from MascotasCore.Carrito import Carrito
import datetime
from django.contrib.auth.models import User
import random
from pyexpat.errors import messages
from django.contrib import messages
# Create your views here.


def index(request):

    return render(request, 'index.html')


def somos(request):
    return render(request, 'somos.html')


def galeria(request):
    return render(request, 'galeria.html')


def FormReg(request):
    return render(request, 'FormReg.html')


def FormCont(request):
    return render(request, 'FormCont.html')


def Api(request):
    return render(request, 'Api.html')


def MostrarProducto(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'mostrarProducto.html', datos)


def formProducto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'formProducto.html', datos)


def form_mod_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(
            data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'form_mod_producto.html', datos)


def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect("MostrarProducto")


def MostrarCliente(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, 'mostrarCliente.html', datos)


def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(idCliente=id)
    datos = {
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'form_mod_cliente.html', datos)


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(idCliente=id)
    cliente.delete()
    return redirect("MostrarCliente")


def compras(request):
    productos = Producto.objects.all()
    return render(request, "compras.html", {'productos': productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    return redirect("Compras")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect("Compras")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect("Compras")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Compras")


def formCliente(request):
    datos = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    if (request.method == 'POST'):
        usuario = request.POST['email']
        contrasena = request.POST['contrasena']
        user = User.objects.create(
            username=usuario,
            password=contrasena,
        )
        user.set_password(contrasena)
        user.save()
    return render(request, 'formCliente.html', datos)


def pagar(request):
    if(request.method == 'POST'):
        carro = request.session["carrito"]
        if(len(carro) <= 0):
            return redirect('carrito')
        total = 0
        numeroOrden = random.uniform(100, 999)
        for produ in carro:
         total += int(carro[produ]["acumulado"])

        idUsuario = request.session["_auth_user_id"]
        usuario = User.objects.get(pk=idUsuario)
        fechaCompra = datetime.datetime.now()
        fechaEntrga = fechaCompra+datetime.timedelta(days=7)
        venta = Venta.objects.create(
            nmr_orden=numeroOrden,
            total=total,
            fch_compra=fechaCompra,
            fch_entrega=fechaEntrga,
            idUser=usuario,

        )
        venta.save()
        for produ in carro:
            productoEnCarro = Producto.objects.get(pk=carro[produ]["producto_id"])
            detalle = VentaProducto.objects.create(
                cantidad=carro[produ]["cantidad"],
                orden=venta,
                producto=productoEnCarro,
            )
            detalle.save()
            productoEnCarro.stock -= carro[produ]["cantidad"]
            productoEnCarro.save()
        carrito = Carrito(request)
        carrito.limpiar()
        messages.success(request, 'Pagado Correctamente')
        request.session['nmr_orden'] = int(venta.nmr_orden)     
    return redirect('/compras/')


def mostrarCompras(request):
    ventas = Venta.objects.filter(idUser = request.user).all()
    ctx={}
    if Venta.objects.filter(idUser=request.user).exists():
        ctx['mostrarCompras'] = ventas 
    else:
        messages.success(request, 'No a realizado compras')
    return render(request, 'mostrarCompras.html/',ctx)


def seguimiento(request):
    ctx = {}
    if request.method == 'GET':
        if 'num_pedido' in request.GET:
            num = request.GET['num_pedido']
            if Venta.objects.filter(nmr_orden=num).exists():
                orden = Venta.objects.get(nmr_orden=num)
                ctx['orden'] = orden.__dict__
    return render(request, 'seguimiento.html/', ctx)