from django.db import models

# Create your models here.

#Definicion tabla Persona

class Persona(models.Model):
    id_per = models.IntegerField(primary_key=True, verbose_name='Id persona')
    nombre_per = models.CharField(max_length=50, verbose_name='Nombre persona')
    apellido_per = models.CharField(max_length=30, verbose_name='Apellido persona')
    correo_per = models.CharField(max_length=30, verbose_name='Correo persona')
    clave_per = models.CharField(max_length=20, verbose_name='Clave persona')
    ciudad_per = models.CharField(max_length=30, verbose_name='Ciudad persona')
    region_per = models.CharField(max_length=30, verbose_name='Region persona')
    codPostal_per = models.IntegerField(verbose_name='Codigo postal persona')
    
    def __str__(self):
        return self.nombre_per
    
 #Definicion tabla Empresa  

class Empresa(models.Model):
    id_emp = models.IntegerField(primary_key=True, verbose_name='Id empresa')
    nombre_emp = models.CharField(max_length=50, verbose_name='Nombre empresa')
    razonSocial_emp = models.CharField(max_length=30, verbose_name='Razon social empresa')
    correo_emp = models.CharField(max_length=30, verbose_name='Correo empresa')
    clave_emp = models.CharField(max_length=20, verbose_name='Clave empresa')
    ciudad_emp = models.CharField(max_length=30, verbose_name='Ciudad empresa')
    region_emp = models.CharField(max_length=30, verbose_name='Region empresa')
    giro_emp = models.CharField(max_length=15, verbose_name='Giro empresa')
    
    def __str__(self):
        return self.nombre_emp
  
  
