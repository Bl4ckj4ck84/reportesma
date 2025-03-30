from rest_framework import serializers
from .models import OrganismoSectorial, PPDA, MedidaAvance, Medida, Indicador, Actividad

class OrganismoSectorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganismoSectorial
        fields = '__all__'

class PPDASerializer(serializers.ModelSerializer):
    class Meta:
        model = PPDA
        fields = '__all__'

class MedidaAvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedidaAvance
        fields = '__all__'


from .models import Indicador

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'
        
        
from .models import ReporteAnual

class ReporteAnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteAnual
        fields = '__all__'
        
        
class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'