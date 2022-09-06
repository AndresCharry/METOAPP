from django.urls import path

from Variables import views

urlpatterns = [
    path('formularioNombreVariables/', views.nombreVariables, name = "FormularioNombreVariables" ),
    path('formularioVariables/', views.Variables, name = "FormularioVariables"),
]
