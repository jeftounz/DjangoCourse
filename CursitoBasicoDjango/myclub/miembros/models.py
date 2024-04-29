from django.db import models

# Create your models here.

class Estado(models.Model):
    nb_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nb_estado

class Ciudad(models.Model):
    nb_ciudad = models.CharField(max_length=70)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nb_ciudad

class Municipio(models.Model):
    nb_municipio = models.CharField(max_length=70)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nb_municipio

class Direccion(models.Model):
    nb_calle = models.CharField(max_length=70)
    nb_residencia = models.CharField(max_length=80)
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nb_calle}, {self.nb_residencia}"

class Persona(models.Model):
    nu_cedula = models.IntegerField()
    nb_nombre = models.CharField(max_length=50)
    nb_apellido = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    sexo = models.BooleanField()
    fech_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    nu_telefono = models.IntegerField()
    g_instruccion = models.CharField(max_length=100)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fech_registro = models.DateField()

    def __str__(self):
        return f"{self.nb_nombre} {self.nb_apellido}"