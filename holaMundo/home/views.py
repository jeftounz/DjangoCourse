from django.http import HttpResponse

def homeView(request):
    return HttpResponse("Hola Mundo, esta es mi primera vista!!!")
    