from django.urls import path

from . import views

urlpatterns = [
    path('', views.coordenadas, name = "Coordenadas"),
]
