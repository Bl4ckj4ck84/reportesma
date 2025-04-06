from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.shortcuts import render
from django.http import JsonResponse
from .models import OrganismoSectorial, PPDA, MedidaAvance, Indicador, Actividad, ReporteAnual
from .serializers import (
    OrganismoSectorialSerializer,
    PPDASerializer,
    MedidaAvanceSerializer,
    IndicadorSerializer,
    ActividadSerializer,
    ReporteAnualSerializer,
)
from .snifa_integration import obtener_datos_snifa
from .airecoo_integration import obtener_datos_airecoo
from rest_framework.decorators import api_view, permission_classes

class EsSMAPermission(BasePermission):
    """
    Permiso personalizado para verificar si el usuario tiene el rol 'sma'.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'perfilusuario') and request.user.perfilusuario.rol == 'sma'

class OrganismoSectorialViewSet(viewsets.ModelViewSet):
    queryset = OrganismoSectorial.objects.all()
    serializer_class = OrganismoSectorialSerializer
    permission_classes = [IsAuthenticated]

class PPDAViewSet(viewsets.ModelViewSet):
    queryset = PPDA.objects.all()
    serializer_class = PPDASerializer
    permission_classes = [IsAuthenticated]

class MedidaAvanceViewSet(viewsets.ModelViewSet):
    queryset = MedidaAvance.objects.all()
    serializer_class = MedidaAvanceSerializer
    permission_classes = [IsAuthenticated]

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organismo_responsable=self.request.user.perfilusuario.organismo_responsable)

class ReporteAnualViewSet(viewsets.ModelViewSet):
    queryset = ReporteAnual.objects.all()
    serializer_class = ReporteAnualSerializer
    permission_classes = [EsSMAPermission]

    def perform_create(self, serializer):
        serializer.save(organismo_responsable=self.request.user.perfilusuario.organismo_responsable)

def frontend_view(request):
    return render(request, 'reportes/index.html')

def login_view(request):
    return render(request, 'reportes/login.html')



def guardar_datos_snifa(datos):
    for dato in datos:
        if not all(key in dato for key in ['parametro', 'valor']):
            raise ValueError(f"Datos incompletos en SNIFA: {dato}")
        indicador = Indicador(
            nombre=dato['parametro'],
            valor=dato['valor'],
            unidad="µg/m³",
            organismo_sectorial_id=1
        )
        indicador.save()

@api_view(['POST'])
@permission_classes([EsSMAPermission])
def integrar_snifa(request):
    try:
        datos_snifa = obtener_datos_snifa()
        if not datos_snifa:
            return JsonResponse({"error": "No se recibieron datos de SNIFA."}, status=500)
        guardar_datos_snifa(datos_snifa)
        return JsonResponse({"mensaje": "Datos de SNIFA integrados correctamente."})
    except ValueError as ve:
        return JsonResponse({"error": f"Error de validación: {str(ve)}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Error al integrar datos de SNIFA: {str(e)}"}, status=500)

def guardar_datos_airecoo(datos):
    for dato in datos:
        if not all(key in dato for key in ['nombre', 'valor', 'unidad']):
            raise ValueError(f"Datos incompletos en Airecoo: {dato}")
        indicador = Indicador(
            nombre=dato['nombre'],
            valor=dato['valor'],
            unidad=dato['unidad'],
            organismo_sectorial_id=1
        )
        indicador.save()
        


@api_view(['POST'])
@permission_classes([EsSMAPermission])
def integrar_airecoo(request):
    try:
        datos_airecoo = obtener_datos_airecoo()
        if not datos_airecoo:
            return JsonResponse({"error": "No se recibieron datos de Airecoo."}, status=500)
        guardar_datos_airecoo(datos_airecoo)
        return JsonResponse({"mensaje": "Datos de Airecoo integrados correctamente."})
    except ValueError as ve:
        return JsonResponse({"error": f"Error de validación: {str(ve)}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Error al integrar datos de Airecoo: {str(e)}"}, status=500)