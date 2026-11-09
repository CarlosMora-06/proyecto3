from rest_framework import serializers
from mascotas.models import Responsable,Mascota



class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota

