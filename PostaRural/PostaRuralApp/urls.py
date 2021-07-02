
from django.contrib import admin
from django.urls import path,include
from .views import MostrarInicio,Dashboard,Reserva,crearReserva,NuevaFicha,crearFicha,MostarListaUsuarios,VistaAgregarUsuario,crearUsuario,MostarListaPacientesCronicos
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [

 path('',MostrarInicio ,name="MostrarInicio" ),
 path ('login', LoginView.as_view(template_name='login.html') , name='login' ),
 path('Dashboard',Dashboard ,name="Dashboard" ),
 path('logout', LogoutView.as_view(template_name='login.html'), name='logout'),
 path('reserva',Reserva ,name="reserva" ),
 path('crear_reserva/', crearReserva, name="crear_reserva" ),
 path('Dashboard/NuevaFicha',NuevaFicha ,name="NuevaFicha" ),
 path('Dashboard/crear_ficha/', crearFicha, name="crear_ficha" ),
 path('Dashboard/Usuarios/', MostarListaUsuarios, name="MostarListaUsuarios" ),
 path('Dashboard/Usuarios/Agregar', VistaAgregarUsuario, name="VistaAgregarUsuario" ),
 path('Dashboard/Usuarios/crear_usuario/', crearUsuario, name="crearUsuario" ),
 path('Dashboard/AsignarMedicamento',MostarListaPacientesCronicos ,name="MostarListaPacientesCronicos" ),





]