from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .decorators import unauthenticated_user,allowed_users, admin_only
# Create your views here.
from .models import *
from .forms import CreateUserForm, CrearProveedorForm, ProductoForm
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['cliente'])
def home(request):
    context = {
        'productos': Producto.objects.all()
    }
    return render(request, 'comilon/home.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['proveedor'])
def vistaProveedor(request):
	productos = request.user.proveedor.producto_set.all()
	proveedores = Proveedor.objects.all()
	context = {'productos': productos, 'proveedores': proveedores}
	return render(request, 'comilon/vista_proveedor.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def datos(request):
	ordenes = Orden.objects.all()
	clientes = Cliente.objects.all()
	proveedores = Proveedor.objects.all()

	total_customers = clientes.count()

	total_ordenes = ordenes.count()
	entregado = ordenes.filter(estado='Entregado').count()
	pendiente = ordenes.filter(estado='Pendiente').count()

	context = {'ordenes':ordenes, 'clientes':clientes,
	'total_ordenes':total_ordenes,'entregado':entregado,
	'pendiente':pendiente, 'proveedores':proveedores}

	return render(request, 'comilon/datos.html', context)

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='proveedor')
			user.groups.add(group)
			Cliente.objects.create(
				user=user,
				nombre=user.username,
			)

			messages.success(request, 'Cuenta creada para ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'comilon/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def registrarProveedor(request):

	form = CrearProveedorForm()
	if request.method == 'POST':
		form = CrearProveedorForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='proveedor')
			user.groups.add(group)
			Proveedor.objects.create(
				user=user,
				nombre=user.username,
				)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'comilon/crear_proveedor.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('datos')
		else:
			messages.info(request, 'Usuario o contraseña incorrecta')

	context = {}
	return render(request, 'comilon/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def PaginaProveedor(request, pk):
	proveedor = Proveedor.objects.get(id=pk)

	productos = proveedor.producto_set.all()

	context = {'proveedor': proveedor, 'productos': productos}
	return render(request, 'comilon/proveedor.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['proveedor'])
def crearProducto(request, pk):
	ProductoFormSet = inlineformset_factory(Proveedor, Producto, fields=('nombre', 'precio', 'descripcion'), extra=1)
	proveedor = Proveedor.objects.get(id=pk)
	formset = ProductoFormSet(queryset=Producto.objects.none(),instance=proveedor)
	if request.method == 'POST':
		
		formset = ProductoFormSet(request.POST, instance=proveedor)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'comilon/producto_form.html', context)
