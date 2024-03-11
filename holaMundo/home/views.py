from django.http import HttpResponse
from django.shortcuts import render
from .models import Task #Importamos el modelo a las vistas
def homeView(request):
    #return HttpResponse("Hola Mundo, esta es mi primera vista!!!")
    #Creamos un contexto , un diccionario donde se almacenen valores para renderizar
    context={
        'message':'Hola Mundo, esto esta en el contexto',
        'message2':'Tareas por hacer',
        'tasks':Task.objects.filter(done=False),
        'emptyList':[]
    }

    #print(Task.objects.all())

    return render(request,'home/index.html',context)