from django.db import models
from django.contrib.auth.models import AbstractUser

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Role(models.Model):
    SUPERUSER = 'superuser'
    ADMIN_MUNICIPIO = 'admin_municipio'
    RELEVADOR = 'relevador'
    TECNICO = 'tecnico'

    ROLE_CHOICES = [
        (SUPERUSER, 'Superuser'),
        (ADMIN_MUNICIPIO, 'AdminMunicipio'),
        (RELEVADOR, 'Relevador'),
        (TECNICO, 'Tecnico'),
    ]

    role_name = models.CharField(max_length=100, choices=ROLE_CHOICES, unique=True)
    can_manage_users = models.BooleanField(default=False)
    can_manage_all_relevamientos = models.BooleanField(default=False)
    can_create_relevamientos = models.BooleanField(default=False)
    can_modify_own_relevamientos = models.BooleanField(default=False)
    can_generate_reports = models.BooleanField(default=False)

    def __str__(self):
        return self.get_role_name_display()

class CustomUser(AbstractUser):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_users')

    def __str__(self):
        return self.username

class Especie(models.Model):
    nombre_cientifico = models.CharField(max_length=200)
    nombre_comun = models.CharField(max_length=200)
    origen = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_cientifico

class Altura(models.Model):
    rango_altura = models.CharField(max_length=50)

    def __str__(self):
        return self.rango_altura

class DiametroTronco(models.Model):
    rango_diametro = models.CharField(max_length=50)

    def __str__(self):
        return self.rango_diametro

class EstadoFitosanitario(models.Model):
    nombre_estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_estado

class CondicionesCrecimiento(models.Model):
    nombre_condicion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_condicion

class Arbol(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=100)
    calle = models.CharField(max_length=200)
    numero_aprox = models.IntegerField()
    identificacion = models.CharField(max_length=200)
    barrio = models.CharField(max_length=200)
    altura = models.ForeignKey(Altura, on_delete=models.CASCADE)
    diametro = models.ForeignKey(DiametroTronco, on_delete=models.CASCADE)
    estado_base = models.ForeignKey(EstadoFitosanitario, related_name='estado_base', on_delete=models.SET_NULL, null=True, blank=True)
    estado_copa = models.ForeignKey(EstadoFitosanitario, related_name='estado_copa', on_delete=models.SET_NULL, null=True, blank=True)
    estado_tronco = models.ForeignKey(EstadoFitosanitario, related_name='estado_tronco', on_delete=models.SET_NULL, null=True, blank=True)
    tratamiento_previo = models.TextField(null=True, blank=True)
    cazuela = models.CharField(max_length=100, null=True, blank=True)
    requiere_tratamiento = models.BooleanField(default=False)
    ambito = models.CharField(max_length=50)
    protegido = models.BooleanField(default=False)
    fecha_censo = models.DateField()
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    interferencias = models.TextField(null=True, blank=True)
    detalles_arbol = models.TextField(null=True, blank=True)
    absorcion_co2 = models.FloatField(null=True, blank=True)
    edad = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.identificacion

class TipoInterferencia(models.Model):
    nombre_tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_tipo

class Interferencia(models.Model):
    arbol = models.ForeignKey(Arbol, on_delete=models.CASCADE)
    tipo_interferencia = models.ForeignKey(TipoInterferencia, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.tipo_interferencia} - {self.arbol}"

class Medicion(models.Model):
    arbol = models.ForeignKey(Arbol, on_delete=models.CASCADE)
    fecha_medicion = models.DateField()
    altura = models.ForeignKey(Altura, on_delete=models.CASCADE)
    diametro = models.ForeignKey(DiametroTronco, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=100)
    calle = models.CharField(max_length=200)
    numero_aprox = models.IntegerField()
    barrio = models.CharField(max_length=200)
    estado_copa = models.ForeignKey(EstadoFitosanitario, related_name='medicion_estado_copa', on_delete=models.SET_NULL, null=True, blank=True)
    estado_tronco = models.ForeignKey(EstadoFitosanitario, related_name='medicion_estado_tronco', on_delete=models.SET_NULL, null=True, blank=True)
    estado_base = models.ForeignKey(EstadoFitosanitario, related_name='medicion_estado_base', on_delete=models.SET_NULL, null=True, blank=True)
    condicion = models.ForeignKey(CondicionesCrecimiento, on_delete=models.SET_NULL, null=True, blank=True)
    tratamiento_previo = models.TextField(null=True, blank=True)
    cazuela = models.CharField(max_length=100, null=True, blank=True)
    requiere_tratamiento = models.BooleanField(default=False)
    ambito = models.CharField(max_length=50)
    protegido = models.BooleanField(default=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    interferencias = models.TextField(null=True, blank=True)
    detalles_arbol = models.TextField(null=True, blank=True)
    absorcion_co2 = models.FloatField(null=True, blank=True)
    edad = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Medición de {self.arbol} - {self.fecha_medicion}"

class Foto(models.Model):
    medicion = models.ForeignKey(Medicion, on_delete=models.CASCADE)
    tipo_foto = models.CharField(max_length=100)  # censo, estado_fitosanitario
    ruta_foto = models.CharField(max_length=200)

    class Meta:
        unique_together = ['medicion', 'tipo_foto']

    def __str__(self):
        return f"Foto de {self.medicion} - {self.tipo_foto}"
