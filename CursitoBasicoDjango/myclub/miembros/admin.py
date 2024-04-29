from django.contrib import admin
from .models import Estado,Ciudad,Municipio,Direccion,Persona
# Register your models here.
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Municipio)
admin.site.register(Direccion)
admin.site.register(Persona)
