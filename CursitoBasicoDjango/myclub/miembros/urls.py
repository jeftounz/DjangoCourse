from django.urls import path
from . import views

urlpatterns=[
    path('holamundo/',views.holaMundo,name='holaMundo'),
    path('estadoVenzuela/',views.estadoVenezuela,name='estadoVenezuela'),
    path('registrar_ciudad/',views.ciudadesVenezuela,name='ciudadesVenezuela'),
    path('dashboard/',views.dashboard,name='Dashboard')
] 