from  django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import ReservaHora, UserSalud
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def MostrarInicio(request):
   
   return render(request,'inicio.html')


def login(request):
   return render(request,'login.html')


def NuevaFicha(request):
     current_user = request.user.username
     if UserSalud.objects.filter(username=current_user, user_type='Medico'):
      rol='Medico'
      return render(request,'ficha_clinica.html' ,{'rol_user':rol})
     else:
      return redirect("http://127.0.0.1:8000/")


def Dashboard(request):   
    current_user = request.user.username
    rol=''
    if UserSalud.objects.filter(username=current_user, user_type='Medico'):
        rol='Medico'
        return render(request,'dashboard.html' ,{'username':current_user, 'rol_user':rol})

    elif UserSalud.objects.filter(username=current_user, user_type='Administrador'):
        rol='Administrador'
        return render(request,'dashboard.html' ,{'username':current_user, 'rol_user':rol})

    elif UserSalud.objects.filter(username=current_user, user_type='Paciente'):
        rol='Paciente'
        return render(request,'dashboard.html' ,{'username':current_user, 'rol_user':rol})


    else:
      return redirect("http://127.0.0.1:8000/")


def Reserva(request):
   return render(request,'reservaHora.html')





def Enviar_EmailReserva(user_mail, subject, template_name, context):
    template = get_template(template_name)
    content = template.render(context)

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[
            user_mail
        ],
        cc=[]
    )

    message.attach_alternative(content, 'text/html')
    return message
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
      
        reserva=ReservaHora.objects.create(
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
        if request.method == 'POST': 

         mail = Enviar_EmailReserva(Correo,
        'Codigo Reserva PostRural ',
        'email_reserva.html',
         {
            'nombre': nombres,'codigo':reserva.id
            
         }
    )

    else:
       return JsonResponse({"status": 'error'})     
    
    mail.send(fail_silently=False)
    return JsonResponse({"id_reserva": reserva.id}) 


     
    