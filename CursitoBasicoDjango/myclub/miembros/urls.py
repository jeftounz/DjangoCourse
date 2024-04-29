from django.urls import path
from . import views

urlpatterns=[
    path('holamundo/',views.holaMundo,name='holaMundo'),
    path('estadoVenzuela/',views.estadoVenezuela,name='estadoVenezuela'),
]