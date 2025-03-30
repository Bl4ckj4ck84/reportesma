from django.contrib import admin
from .models import OrganismoSectorial, PPDA, Medida, Indicador, MedidaAvance, ReporteAnual, Actividad

# Registra los modelos en el panel de administración
@admin.register(OrganismoSectorial)
class OrganismoSectorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'telefono')  # Campos que se mostrarán en la lista
    search_fields = ('nombre',)  # Permite buscar por nombre

@admin.register(PPDA)
class PPDAAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_inicio', 'fecha_termino', 'organismo')
    list_filter = ('organismo',)  # Filtrar por organismo

@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'prioridad', 'organismo_responsable')
    list_filter = ('tipo', 'prioridad')

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'valor', 'unidad', 'organismo_sectorial', 'ppda')
    search_fields = ('nombre',)

@admin.register(MedidaAvance)
class MedidaAvanceAdmin(admin.ModelAdmin):
    list_display = ('medida', 'descripcion', 'avance', 'estado')
    list_filter = ('estado',)

@admin.register(ReporteAnual)
class ReporteAnualAdmin(admin.ModelAdmin):
    list_display = ('organismo_responsable', 'periodo', 'cumplimiento')
    list_filter = ('periodo',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_termino', 'organismo_responsable')
    search_fields = ('nombre',)