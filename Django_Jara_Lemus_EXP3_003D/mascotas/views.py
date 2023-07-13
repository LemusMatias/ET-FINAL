from django.shortcuts import render, redirect
from .models import *
from .forms import MascotaForm, RegistroUserForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from mascotas.compra import Carrito 
from django.contrib import messages

# Create your views here.

def principal(request):
    return render(request, 'principal.html')

def productos(request):
    return render(request, 'productos.html')

def quiensomos(request):
    return render (request, 'quiensomos.html')
def feriados(request):
    return render (request, 'feriados.html')

@login_required
def almacen(request):
 
    producto=Producto.objects.all()    #obtenemos todos los obj de la clase Vehiculo
    datos={'mascotitas' : producto}     #creamos diccionario que recibe la colección de objetos
    return render(request, 'almacen.html', datos)   #enviamos parámetro al template


@login_required
def crear(request):
    if request.method=='POST':
        mascotaform = MascotaForm(request.POST, request.FILES)
        if mascotaform.is_valid():
            mascotaform.save()     #similar al insert en función
            return redirect('almacen')
    else:
        mascotaform=MascotaForm()
    
    
    return render(request, 'crear.html',{'mascotaform': mascotaform})


@login_required
def eliminar(request, id):
    productoEliminado=Producto.objects.get(idproducto=id)  #obtenemos un objeto por su pk
    productoEliminado.delete()
    return redirect('almacen')


@login_required
def modificar(request,id):
    productos = Producto.objects.get(idproducto=id)         #obtenemos un objeto por su pk
    datos ={
        'form':MascotaForm(instance=productos)
    }
    if request.method=='POST':
        formulario = MascotaForm(data=request.POST, instance=productos)
        if formulario.is_valid:
            formulario.save()
            return redirect ('almacen')
    return render(request, 'modificar.html', datos)

def registrar(request):
    data={
        'form' : RegistroUserForm()
    }
    if request.method == 'POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('principal')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


@login_required
def mostrar(request):
    mascotitas =Producto.objects.all()
    datos={
        'mascotitas' : mascotitas
    }
    return render(request,'mostrar.html',datos)


@login_required
def carrito(request):
    return render(request, 'carrito.html')

@login_required
def tienda(request):
    producto = Producto.objects.all()
    datos={
        'producto': producto
    }
    return render(request, 'tienda.html', datos)

@login_required
def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idproducto= id)
    carrito_compra.agregar(producto = producto)
    return redirect('tienda')



@login_required
def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idproducto=id)
    carrito_compra.eliminar(producto = producto)
    return redirect('tienda')



@login_required
def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idproducto=id)
    carrito_compra.restar(producto = producto)
    return redirect('tienda')



@login_required
def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    



@login_required
def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(idproducto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            if cant <= producto.stock:
                producto.stock -= cant
            producto.save()   
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }

    return render(request, 'detallecarrito.html',datos)
