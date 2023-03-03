from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # type: ignore 
    path('property/<str:id>', views.imovel, name='property')

 ]# type: ignore
