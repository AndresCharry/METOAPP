from django.urls import path

from BaseDatos import views

urlpatterns = [
    path('encuestaBaseDatos/', views.EncuestaBaseDatos, name = "EncuestaBaseDatos"),
    path('nuevoProyecto/', views.NuevoProyecto, name = "NuevoProyecto"),
    path('nuevoProyecto2/', views.NuevoProyecto2, name = "NuevoProyecto2"),
    path('nuevoProyecto3/', views.NuevoProyecto3, name = "NuevoProyecto3"),
    path('tipoProyecto/', views.TipoDeProyecto, name = "TipoProyecto"),
    path('baseDatos/', views.BaseDatos, name = "BaseDatos"),
    path('baseDatos2/', views.BaseDatos2, name = "BaseDatos2"),
    path('baseDatos3/', views.BaseDatos3, name = "BaseDatos3"),
    path('finalizar/', views.Finalizar, name = 'Finalizar' ),
    path('finalizarBaseDatos/', views.FinalizarBaseDeDatos, name = 'FinalizarBaseDatos' ),
]
