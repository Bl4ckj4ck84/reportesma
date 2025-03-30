
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from reportes.views import frontend_view
from reportes.views import integrar_snifa


schema_view = get_schema_view(
   openapi.Info(
      title="Sistema de Reportes Ambientales API",
      default_version='v1',
      description="API para el sistema de reportes ambientales de Chile",
      contact=openapi.Contact(email="contacto@reportesambientales.cl"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reportes.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('frontend/', frontend_view, name='frontend'),
    path('integrar-snifa/', integrar_snifa, name='integrar_snifa')
]
