from django.urls import path

from . import views

urlpatterns = [
    path('coordenadas', views.coordenadas, name = "Coordenadas"),
    path('vista/', views.vista, name = "Vista")
]
