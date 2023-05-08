from rest_framework import serializers
from app.models import Personas

#personalizacion de Tabla Persona hacia json
class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields =['id_per','nombre_per','apellido_per','correo_per','clave_per','codPostal_per']


class PersonaSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields =['id_per','nombre_per','apellido_per','correo_per','clave_per','codPostal_per']