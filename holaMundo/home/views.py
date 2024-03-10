from django.http import HttpResponse
from django.shortcuts import render

def homeView(request):
    #return HttpResponse("Hola Mundo, esta es mi primera vista!!!")
    #Creamos un contexto , un diccionario donde se almacenen valores para renderizar
    context={
        'message':'Hola Mundo, esto esta en el contexto',
        'message2':'Tareas por hacer',
        'tasks':["Mapa","Video","Resumen","Dibujo"],
        'emptyList':[]
    }

    return render(request,'home/index.html',context)