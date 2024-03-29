from django.shortcuts import render
from .models import TareaNueva

def index(request):
    tareas = TareaNueva.objects.all()
    return render(request,'index.html',{'tareas':tareas})
