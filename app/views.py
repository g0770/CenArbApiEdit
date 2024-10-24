from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from .models import (
    Provincia, CustomUser, Municipio, Especie, Arbol, EstadoFitosanitario, 
    Altura, DiametroTronco, Role, Interferencia, Medicion, Foto, CondicionesCrecimiento, TipoInterferencia
)
from .serializers import (
    ProvinciaSerializer, MunicipioSerializer, EspecieSerializer, ArbolSerializer, 
    UserSerializer, EstadoFitosanitarioSerializer, AlturaSerializer, DiametroTroncoSerializer, 
    RoleSerializer, InterferenciaSerializer, MedicionSerializer, FotoSerializer, 
    CondicionesCrecimientoSerializer, TipoInterferenciaSerializer
)
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la API de App Arbolado")

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todos los usuarios",
        responses={200: UserSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de un usuario por su ID",
        responses={200: UserSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(CustomUser, pk=kwargs['pk'])
        serializer = UserSerializer(instance)
        return Response(serializer.data)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todos los roles",
        responses={200: RoleSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de un rol por su ID",
        responses={200: RoleSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Role, pk=kwargs['pk'])
        serializer = RoleSerializer(instance)
        return Response(serializer.data)

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todas las provincias",
        responses={200: ProvinciaSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de una provincia por su ID",
        responses={200: ProvinciaSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Provincia, pk=kwargs['pk'])
        serializer = ProvinciaSerializer(instance)
        return Response(serializer.data)

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todos los municipios",
        responses={200: MunicipioSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de un municipio por su ID",
        responses={200: MunicipioSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Municipio, pk=kwargs['pk'])
        serializer = MunicipioSerializer(instance)
        return Response(serializer.data)

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todas las especies",
        responses={200: EspecieSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de una especie por su ID",
        responses={200: EspecieSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Especie, pk=kwargs['pk'])
        serializer = EspecieSerializer(instance)
        return Response(serializer.data)

class ArbolViewSet(viewsets.ModelViewSet):
    queryset = Arbol.objects.all()
    serializer_class = ArbolSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todos los árboles",
        responses={200: ArbolSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de un árbol por su ID",
        responses={200: ArbolSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Arbol, pk=kwargs['pk'])
        serializer = ArbolSerializer(instance)
        return Response(serializer.data)

class EstadoFitosanitarioViewSet(viewsets.ModelViewSet):
    queryset = EstadoFitosanitario.objects.all()
    serializer_class = EstadoFitosanitarioSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todos los estados fitosanitarios",
        responses={200: EstadoFitosanitarioSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de un estado fitosanitario por su ID",
        responses={200: EstadoFitosanitarioSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(EstadoFitosanitario, pk=kwargs['pk'])
        serializer = EstadoFitosanitarioSerializer(instance)
        return Response(serializer.data)

class AlturaViewSet(viewsets.ModelViewSet):
    queryset = Altura.objects.all()
    serializer_class = AlturaSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todas las alturas",
        responses={200: AlturaSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de una altura por su ID",
        responses={200: AlturaSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Altura, pk=kwargs['pk'])
        serializer = AlturaSerializer(instance)
        return Response(serializer.data)

class DiametroTroncoViewSet(viewsets.ModelViewSet):
    queryset = DiametroTronco.objects.all()
    serializer_class = DiametroTroncoSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todos los diámetros de tronco",
        responses={200: DiametroTroncoSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de un diámetro de tronco por su ID",
        responses={200: DiametroTroncoSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(DiametroTronco, pk=kwargs['pk'])
        serializer = DiametroTroncoSerializer(instance)
        return Response(serializer.data)

class CondicionesCrecimientoViewSet(viewsets.ModelViewSet):
    queryset = CondicionesCrecimiento.objects.all()
    serializer_class = CondicionesCrecimientoSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todas las condiciones de crecimiento",
        responses={200: CondicionesCrecimientoSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de una condición de crecimiento por su ID",
        responses={200: CondicionesCrecimientoSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(CondicionesCrecimiento, pk=kwargs['pk'])
        serializer = CondicionesCrecimientoSerializer(instance)
        return Response(serializer.data)

class TipoInterferenciaViewSet(viewsets.ModelViewSet):
    queryset = TipoInterferencia.objects.all()
    serializer_class = TipoInterferenciaSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todos los tipos de interferencia",
        responses={200: TipoInterferenciaSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de un tipo de interferencia por su ID",
        responses={200: TipoInterferenciaSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(TipoInterferencia, pk=kwargs['pk'])
        serializer = TipoInterferenciaSerializer(instance)
        return Response(serializer.data)

class InterferenciaViewSet(viewsets.ModelViewSet):
    queryset = Interferencia.objects.all()
    serializer_class = InterferenciaSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todas las interferencias",
        responses={200: InterferenciaSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de una interferencia por su ID",
        responses={200: InterferenciaSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Interferencia, pk=kwargs['pk'])
        serializer = InterferenciaSerializer(instance)
        return Response(serializer.data)

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todas las mediciones",
        responses={200: MedicionSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de una medición por su ID",
        responses={200: MedicionSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Medicion, pk=kwargs['pk'])
        serializer = MedicionSerializer(instance)
        return Response(serializer.data)

class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene una lista de todas las fotos",
        responses={200: FotoSerializer(many=True), 400: 'Bad Request'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene detalles de una foto por su ID",
        responses={200: FotoSerializer(), 404: 'Not Found'}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Foto, pk=kwargs['pk'])
        serializer = FotoSerializer(instance)
        return Response(serializer.data)
