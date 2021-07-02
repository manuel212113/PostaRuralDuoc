from  django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import FichaPaciente, ReservaHora, UserSalud,UserSaludManager
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



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





def Enviar_Email(user_mail, subject, template_name, context):
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

         mail = Enviar_Email(Correo,
        'Codigo Reserva PostRural ',
        'email_reserva.html',
         {
            'nombre': nombres.upper(),'codigo':reserva.id
            
         }
    )

    else:
       return JsonResponse({"status": 'error'})     
    
    mail.send(fail_silently=False)
    return JsonResponse({"id_reserva": reserva.id}) 


     
def crearFicha(request):

           
    if request.method == 'POST': 
        rut = request.POST.get('rut_paciente') 
        nombres = request.POST.get('Nombres')
        apellidos = request.POST.get('Apellidos')
        estadoCivil=request.POST.get('EstadoCivil')
        Pais= request.POST.get('Pais')
        genero=request.POST.get('Genero')
        Celular=request.POST.get('Celular')
        Correo=request.POST.get('Correo')
        region=request.POST.get('Region')
        comuna=request.POST.get('Comuna')
        direccion=request.POST.get('Direccion')
        nacimiento=request.POST.get('Nacimiento')
        EnfermedadesCroni=request.POST.get('EnfermedadesCronicas')
        alergias=request.POST.get('AlergiasPaciente')
        NombreAcompañante=request.POST.get('NombreAcompañante')
        ApellidoAcompañante=request.POST.get('ApellidoAcompañante')
        Relacion=request.POST.get('Relacion')
        CelularAcompañante=request.POST.get('CelularAcompañante')

        reserva=FichaPaciente.objects.create(
            rut_paciente=rut,
            Nombres=nombres,
            Apellidos=apellidos,
            nacionalidad=Pais,
            Genero=genero,
            comuna=comuna,
            direccion=direccion,
            nacimiento=nacimiento,
            EnfermedadesCronicas=EnfermedadesCroni,
            Alergias=alergias,
            AcompañanteNombre=NombreAcompañante,
            AcompañanteApellido=ApellidoAcompañante,
            RelacionAcompañante=Relacion,
            celularAcompañante=CelularAcompañante,
            celular=Celular,
            correo=Correo,
            estado_civil=estadoCivil,
            region=region,

        )
      

    else:
       return JsonResponse({"status": 'error'})     
    
    return JsonResponse({"status": "correcto"}) 



def MostarListaUsuarios(request):
     all_users={}
     all_users = UserSalud.objects.values()
     all_users = list(all_users)
     rol='Administrador'
     return render(request,'ListaUsuarios.html', {'ListUsers':all_users,'rol_user':rol})


def VistaAgregarUsuario(request):
    rol='Administrador'
    return render(request,'AgregarUsuario.html',{'rol_user':rol})


def crearUsuario(request):
           
    if request.method == 'POST': 
        
        rut = request.POST.get('rut') 
        nombres = request.POST.get('nombre')
        apellidos = request.POST.get('apellido')
        celular= request.POST.get('celular')
        tipousuario=request.POST.get('tipousuario')
        Correo=request.POST.get('correo')
        nombre_usuario=nombres[:2] +"."+ apellidos[:2]
        password = UserSalud.objects.make_random_password(length=6, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
        
        usuario=UserSalud.objects.create(
            RUT=rut,
            name=nombres,
            last_name=apellidos,
            user_type=tipousuario,
            numero_telefono=celular,
            email=Correo,
            username=nombre_usuario
            
        )
        usuario.set_password(password)
        usuario.save()

        mail = Enviar_Email(Correo,
        'Bienvenido a PostRural ',
        'email_nuevacuenta.html',
         {
            'nombre': nombres.upper() , 'usuario':nombre_usuario,'pass':password
            
         }
        )

    else:
       return JsonResponse({"status": 'error'})     
    
    mail.send(fail_silently=False)
    return JsonResponse({"status": "correcto"}) 




def MostarListaPacientesCronicos(request):
     all_users={}
     all_users = FichaPaciente.objects.values().exclude( EnfermedadesCronicas="Sin Enfermedades").exclude(EnfermedadesCronicas="")
     all_users = list(all_users)
     rol='Medico'
     return render(request,'AsignarMedicamentos.html', {'ListUsers':all_users,'rol_user':rol})
