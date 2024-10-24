from rest_framework import serializers
from .models import (
    Provincia, CustomUser, Municipio, Especie, Arbol, EstadoFitosanitario, 
    Altura, DiametroTronco, Role, Interferencia, Medicion, Foto, CondicionesCrecimiento, TipoInterferencia
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'

class ArbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbol
        fields = '__all__'

class EstadoFitosanitarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoFitosanitario
        fields = '__all__'

class AlturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Altura
        fields = '__all__'

class DiametroTroncoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiametroTronco
        fields = '__all__'

class CondicionesCrecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicionesCrecimiento
        fields = '__all__'

class TipoInterferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInterferencia
        fields = '__all__'

class InterferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interferencia
        fields = '__all__'

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = '__all__'

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'
