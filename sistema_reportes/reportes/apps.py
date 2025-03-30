from django.apps import AppConfig


class ReportesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reportes'


class ReportesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reportes'

    def ready(self):
        import reportes.signals  # Importa las señales
        
# También puedes asignar roles manualmente a través del shell de Django: 

#python manage.py shell

# from django.contrib.auth.models import User
#from reportes.models import PerfilUsuario

# Obtener un usuario
#usuario = User.objects.get(username="nombre_de_usuario")

# Crear o actualizar su perfil
#perfil, creado = PerfilUsuario.objects.get_or_create(user=usuario)
#perfil.rol = "sma"  # Asignar el rol 'sma'
#perfil.save() '''