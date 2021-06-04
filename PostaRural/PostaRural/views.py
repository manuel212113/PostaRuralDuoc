from  django.http import HttpResponse
from django.shortcuts import render,redirect


def MostrarInicio(request):
   
   return render(request,'inicio.html')


def MostrarLogin(request):
   return render(request,'login.html')
