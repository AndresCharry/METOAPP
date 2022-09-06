from django.urls import path

from . import views

urlpatterns = [
    path('', views.encuesta2, name = "Encuesta2"),
]
