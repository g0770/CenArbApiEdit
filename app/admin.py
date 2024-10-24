from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import (
    Provincia, Municipio, Especie, CustomUser, Altura, DiametroTronco, 
    EstadoFitosanitario, CondicionesCrecimiento, Arbol, TipoInterferencia, 
    Interferencia, Medicion, Foto, Role
)

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Related info'), {'fields': ('municipio', 'created_by', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'municipio', 'is_active', 'is_staff', 'is_superuser', 'role'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'municipio', 'is_staff', 'is_active', 'date_joined', 'role')
    search_fields = ('email', 'first_name', 'last_name', 'username')
    ordering = ('email',)

admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Especie)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Altura)
admin.site.register(DiametroTronco)
admin.site.register(EstadoFitosanitario)
admin.site.register(CondicionesCrecimiento)
admin.site.register(Arbol)
admin.site.register(TipoInterferencia)
admin.site.register(Interferencia)
admin.site.register(Medicion)
admin.site.register(Foto)
admin.site.register(Role)
