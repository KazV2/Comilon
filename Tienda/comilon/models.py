from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):

	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	fec_creado = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.nombre


class Proveedor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=30, null=True)
    precio = models.FloatField(null=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    fec_creado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre

class Orden(models.Model):

	ESTADO = (
			('Pendiente', 'Pendiente'),
			('En camino', 'En camino'),
			('Entregado', 'Entregado'),
			)

	cliente = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL)
	producto = models.ForeignKey(Producto, null=True, on_delete= models.SET_NULL)
	fec_creado = models.DateTimeField(auto_now_add=True, null=True)
	estado = models.CharField(max_length=200, null=True, choices=ESTADO)
	nota = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.producto.nombre



	
