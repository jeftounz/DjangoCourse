from django.db import models

# Create your models here.
#En cada modulo que se cree en django , por ejemplo el modulo "home" vas a necesitar ampliar la base de datos
#Las bases de datos van a ser ejecutadas aqui por medio de clases 

#Siempre se crea un modelo con models.Model
class Task(models.Model):
    description=models.CharField(max_length=255)
    done=models.BooleanField(default=False)

#NOTA:cada vez que hacemos una migracion utilizando el manage.py 
#Los modelos creados aqui se conviernten en tablas de SQL lite