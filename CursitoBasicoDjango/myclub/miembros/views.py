from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Estado,Ciudad,Municipio,Direccion,Persona
from .forms import CiudadForm
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
    
def ciudadesVenezuela(request):
    if request.method == 'POST':
        # Si el formulario se envió (es decir, si el método de solicitud es POST),
        # procesa los datos del formulario
        form = CiudadForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda los datos en la base de datos
            form.save()
            print("Datos del formulario recibidos:", form.cleaned_data)
            # Redirige a una página de éxito o a la misma página
            return redirect('ciudadesVenezuela')  # Puedes redirigir a la misma página para mostrar el formulario vacío de nuevo
    else:
        # Si el método de solicitud no es POST, crea un formulario vacío
        form = CiudadForm()
    
    # Renderiza el template con el formulario y la lista de estados
    context = {
        'form': form,
        'estados': Estado.objects.all()
    }
    return render(request, "ciudades.html", context)

def dashboard(request):
    
    template=loader.get_template('dashboard.html')
    context={
    }

    return HttpResponse(template.render(context, request))


