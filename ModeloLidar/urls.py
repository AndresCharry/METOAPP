from django.urls import path

from ModeloLidar import views

urlpatterns = [
    path('formularioModelo/', views.formularioModelo, name = "FormularioModelo"),
    path('formularioModelo2/', views.formularioModelo2, name = "FormularioModelo2"),
    path('vistaModelo/', views.VistaModelo, name = "VistaModelo"),
]
