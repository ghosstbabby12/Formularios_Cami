from django.contrib import admin
from django.urls import path
from . import views
from asistencia import views as asistencia_views
from solicitudes import views as solicitudes_views

urlpatterns = [
    path('', views.home, name='home'),
    path('entrar-admin/', views.admin_login, name='admin_login'),

    path('admin/', admin.site.urls),

    path('asistencia/', asistencia_views.registrar_asistencia, name='registrar_asistencia'),
    path('asistencia/confirmacion/', asistencia_views.confirmacion_asistencia, name='confirmacion_asistencia'),

    path('solicitudes/', solicitudes_views.registrar_solicitud, name='registrar_solicitud'),
    path('solicitudes/confirmacion/', solicitudes_views.confirmacion_solicitud, name='confirmacion_solicitud'),
]
