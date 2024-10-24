from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.shortcuts import redirect
from app import views

# Configuración del router para tus ViewSets
router = DefaultRouter()
router.register(r'provincias', views.ProvinciaViewSet)
router.register(r'municipios', views.MunicipioViewSet)
router.register(r'especies', views.EspecieViewSet)
router.register(r'arboles', views.ArbolViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'estados-fitosanitarios', views.EstadoFitosanitarioViewSet)
router.register(r'alturas', views.AlturaViewSet)
router.register(r'diametros-tronco', views.DiametroTroncoViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'condiciones-crecimiento', views.CondicionesCrecimientoViewSet)
router.register(r'tipos-interferencia', views.TipoInterferenciaViewSet)
router.register(r'interferencias', views.InterferenciaViewSet)
router.register(r'mediciones', views.MedicionViewSet)
router.register(r'fotos', views.FotoViewSet)

# Configuración de Swagger/OpenAPI con JWT Bearer Token
schema_view = get_schema_view(
    openapi.Info(
        title="Documentación API",
        default_version='v1',
        description="Documentación interactiva de la API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@miapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Incluye las rutas de la API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Redirigir la raíz a Swagger
    path('', lambda request: redirect('/swagger/', permanent=True)),

    # Rutas para la documentación de Swagger/OpenAPI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
