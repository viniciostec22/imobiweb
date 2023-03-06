from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # type: ignore 
    path('property/<str:id>', views.imovel, name='property'),
    path('agendar_visitas/', views.agendar_vistas, name='agendar_visitas'),
    path('agendamentos', views.agendamentos, name="agendamentos"),
    path('cancelar_agendamento/<str:id>', views.cancelar_agendamento, name="cancelar_agendamento")

 ]
