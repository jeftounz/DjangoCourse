from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Estado
# Create your views here

def holaMundo(request):
    template=loader.get_template('primer.html')
    return HttpResponse(template.render()) 
    #Fijate que como es simple no necesita que el template.render tenga un "request"

def estadoVenezuela(request):
    venezuela_estados = Estado.objects.all().values()
    template=loader.get_template('estados.html')
    context={
        'venezuela_estados':venezuela_estados
    }
    return HttpResponse(template.render(context, request))
    #Aqui si hay respuesta, porque hay un intercambio de datos entre los datos del modelo y la plantilla html, mediante la vista
    