from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ciberseguridad/', views.ciberseguridad, name='ciberseguridad'),
    path('proyectos/', views.proyectos, name='proyectos'),
]