from django.db import models



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
    