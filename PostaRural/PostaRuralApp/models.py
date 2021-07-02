from django.db import models


from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserSaludManager(BaseUserManager):
    def create_user(self,email,username,name,user_type,last_name,RUT,password = None):
        if not email:
            raise ValueError('El Usuario debe tener un correo Electronico')

        user=self.model(
         username=username,
         email=self.normalize_email(email), 
         name=name,
         RUT=RUT,
         last_name=last_name,
         user_type=user_type
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,name,last_name,RUT,user_type,password):
        user=self.create_user(
         email , 
         username=username,
         name=name, 
         last_name=last_name,
         RUT=RUT,
         user_type=user_type,
         password=password


        )
        if(user_type=='Administrador'):   
            user.admin_user=True
        elif(user_type=='Medico'):
            user.admin_user=False
        else:
            user.user_type='Paciente'
            user.admin_user=False


        user.save()
        return user
       

class UserSalud(AbstractBaseUser):
     username=models.CharField('Nombre de usuario', unique=True,max_length=100)
     email=models.EmailField('Correo Electronico',max_length=254,unique=True)
     name=models.CharField('Nombre',max_length=200,blank=False,null=False)
     last_name=models.CharField('Apellido',max_length=200)
     user_type=models.CharField('Tipo usuario(Medico,Paciente,Administrador)', max_length=300, default='Medico')
     numero_telefono=models.CharField(max_length=15,default="0")
     state_account = models.BooleanField( default=True)
     RUT=models.CharField('RUT',max_length=13 , unique=True)
     admin_user = models.BooleanField( default=False)
     objects=UserSaludManager() 
     
     USERNAME_FIELD= 'username'

     REQUIRED_FIELDS=['email','name','last_name','RUT','user_type']

     class Meta:
          verbose_name_plural="RUT"
     def __str__(self):
          return self.RUT
     def has_perm(self,obj=None):
         return True

     def has_module_perms(self,app_label):
         return True 

     @property
     def is_staff(self):
         return self.admin_user 



class ReservaHora(models.Model):
    rut_paciente=models.CharField('RUT Paciente',max_length=15,null=False)
    Nombres=models.CharField('Nombres del Paciente', max_length=250 )
    Apellidos=models.CharField('Apellidos del Paciente', max_length=250)
    Fecha_reserva=models.CharField('Fecha Reserva',max_length=300)
    Hora_reserva=models.CharField('Hora Reserva',max_length=300)
    celular=models.CharField('Celular',max_length=300, default="Sin Celular")
    correo=models.CharField('Email Paciente',max_length=300)
    especialidad=models.CharField('Especialidad',max_length=300)
    motivo_consulta=models.CharField('Motivo Consulta',max_length=300)
    Medico_asignado=models.CharField('Medico ',max_length=300, default="Sin Asignar")
    

class FichaPaciente(models.Model):
    rut_paciente=models.CharField('RUT Paciente',max_length=15,null=False)
    Nombres=models.CharField('Nombres del Paciente', max_length=250 )
    Apellidos=models.CharField('Apellidos del Paciente', max_length=250)
    Genero=models.CharField('genero del Paciente', max_length=250)
    celular=models.CharField('Celular',max_length=300, default="Sin Celular")
    estado_civil=models.CharField('estado civil',max_length=300, default="Soltero")
    comuna=models.CharField('comuna del Paciente', max_length=250)
    region=models.CharField('region del Paciente', max_length=250)
    direccion=models.CharField('direccion del Paciente', max_length=250)
    nacimiento=models.CharField('fecha nacimiento del Paciente', max_length=250)
    nacionalidad=models.CharField('nacionalidad del Paciente', max_length=250)
    correo=models.CharField('correo del Paciente', max_length=250)
    EnfermedadesCronicas=models.CharField('enfermedades cronicas del Paciente', max_length=250 , default="Sin Enfermedades")
    Alergias=models.CharField('alergias del Paciente', max_length=250, default="Sin Alergias")
    AcompañanteNombre=models.CharField('nombre  del acompañante', max_length=250)
    AcompañanteApellido=models.CharField('apellido  del acompañante', max_length=250)
    RelacionAcompañante=models.CharField('relacion con el Paciente', max_length=250)
    celularAcompañante=models.CharField('celular  del acompañante del paciente', max_length=250)
