from django.contrib import admin
from .models import Task #Importamos los modelos creados

# Register your models here.
#Modelo que hagas lo registraras aqui para que se pueda visualizar en el dashboard de admin
admin.site.register(Task) #Una vez registrada en el dashboard se puede 
#visualizar en el dashboard por defecto que tiene la app admin de django
#y puedes realizar cruds en ella , en base a los campos existentes 
