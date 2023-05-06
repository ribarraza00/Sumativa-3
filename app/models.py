from django.db import models

# Create your models here.

 #Definicion tabla PROFECION

class Profecion(models.Model):
    id_profecion = models.IntegerField(primary_key=True, verbose_name='Id profecion')
    nombreProfecion = models.CharField(max_length=50, verbose_name= 'Profecion')
    def __str__(self):
        return self.nombreProfecion

 #Definicion tabla COMUNA
   
class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True, verbose_name='Id comuna')
    nombreComuna = models.CharField(max_length=50, verbose_name= 'Comuna')
    def __str__(self):
        return self.nombreComuna
    
 #Definicion tabla REGION  

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True, verbose_name='Id region')
    nombreRegion = models.CharField(max_length=50, verbose_name= 'Region')

    def __str__(self):
        return self.nombreRegion
    
#Definicion tabla Persona

class Personas(models.Model):
    id_per = models.IntegerField(primary_key=True, verbose_name='Rut usuario')
    nombre_per = models.CharField(max_length=50, verbose_name='Primer nombre')
    apellido_per = models.CharField(max_length=30, verbose_name='Primer apellido')
    correo_per = models.CharField(max_length=30, verbose_name='Correo')
    clave_per = models.CharField(max_length=20, verbose_name='Contraseña')
    codPostal_per = models.IntegerField(verbose_name='Codigo postal')
    Region = models.ForeignKey(Region, on_delete=models.PROTECT,null=True)
    Comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT,null=True)
    Profecion = models.ForeignKey(Profecion, on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.nombre_per
    



  
  
  
