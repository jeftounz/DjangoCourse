#Aqui agregamos las url para ver las vistas que hay en el modelo
from django.urls import path, reverse #Aqui importamos las path del proyecto original
from .views import homeView, sum_view, create_task #Aqui importamos la vista de urls de esta carpeta oh modulo(home)
urlpatterns=[
    path('',homeView,name='home'),
    path('suma/<int:num1>/<int:num2>',sum_view,name='sum'),
    path('create_task/',create_task,name='create-task') 
]

#NOTA: todas las urls como el de arriba ("path('',homeView,name='home') ", 
#deben ser incluidas en el archivo url.py del modulo original (el holaMundo en este caso)