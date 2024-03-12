from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
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

def sum_view(request,num1,num2):
    sum=num1+num2
    context={
        'sum':sum
    }

    return render(request,'home/sum.html',context)

#Vista del template create_task.html 
def create_task(request):

    if request.POST:
        new_task=request.POST.get('tarea')
       # print("*******")
       # print(new_task)
       #print("*******")
        Task.objects.create(decription=new_task)
        return redirect(reversed('create-task'))

    return render(request,'home/create_task.html')