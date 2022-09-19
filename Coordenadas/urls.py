from django.urls import path

from . import views

urlpatterns = [
    path('coordenadas/', views.coordenadas, name = "Coordenadas"),
    path('upload/', views.archivos, name = "Upload")
]
