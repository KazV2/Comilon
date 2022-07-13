from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
    path('', views.datos, name="datos"),

    path('vista_proveedor/', views.vistaProveedor, name='vista_proveedor'),
    path('proveedor/<str:pk>/', views.PaginaProveedor, name="PaginaProveedor"),
    path('registrar_proveedor', views.registrarProveedor, name="proveedor"),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),

    path('crear_producto/<str:pk>/', views.crearProducto, name="crear_producto"),
]
