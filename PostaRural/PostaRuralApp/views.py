from  django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import ReservaHora

def MostrarInicio(request):
   
   return render(request,'inicio.html')


def login(request):
   return render(request,'login.html')



def Dashboard(request):
   return render(request,'dashboard.html')


def Reserva(request):
   return render(request,'reservaHora.html')



def crearReserva(request):
    if request.method == 'POST': 
        rut = request.POST.get('rut_paciente') 
        nombres = request.POST.get('Nombres')
        apellidos = request.POST.get('Apellidos')
        fecha_reserva= request.POST.get('Fecha_reserva')
        hora_reserva=request.POST.get('Hora_reserva')
        Celular=request.POST.get('celular')
        Correo=request.POST.get('correo')
        Especialidad=request.POST.get('especialidad')
        Motivo_consulta=request.POST.get('motivo_consulta')
        ReservaHora.objects.create(
            rut_paciente=rut,
            Nombres=nombres,
            Apellidos=apellidos,
            Fecha_reserva=fecha_reserva,
            Hora_reserva=hora_reserva,
            celular=Celular,
            correo=Correo,
            especialidad=Especialidad,
            motivo_consulta=Motivo_consulta

        )
    return JsonResponse({"status": 'Success'}) 