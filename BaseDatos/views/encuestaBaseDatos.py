from django.shortcuts import render

# Create your views here.

def EncuestaBaseDatos(request):

    return render(request, "BaseDatos/EncuestaBaseDatos.html")