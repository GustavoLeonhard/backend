"""
Main URL configuration for the school administration system.
"""
from django.urls import path, include
from .views import home

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('institutions/', include('core.urls.institution')),
    path('teachers/', include('core.urls.teacher')),
    # Agregar más rutas aquí según sea necesario
] 