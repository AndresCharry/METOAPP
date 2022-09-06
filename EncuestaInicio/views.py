from django.shortcuts import render, redirect

from .forms import FormularioEncuestaInicio
from .baseDeDatos import baseDeDatos
# Create your views here.


def encuestaInicio(request):
    formulario_encuesta_inicio = FormularioEncuestaInicio()

    if request.method == "POST":
        formulario_encuesta_inicio = FormularioEncuestaInicio(data=request.POST)

        if formulario_encuesta_inicio.is_valid():
            # creaccion del diccionario
            datos= {}
            datos['tipo de cultivo'] = request.POST.get("tipo_cultivo")
            surco = request.POST.get("surcos")
            if surco == "on":
                surco = True
            else:
                surco = False
            datos['surcos'] = surco
            lidar = request.POST.get("lidar")
            if lidar == "on":
                lidar = True
            else:
                lidar = False
            datos['lidar'] = lidar
        
            baseDeDatos.datos(datos)
            return redirect("/encuestaInicio/?valido")

    return render(request, "EncuestaInicio/encuestaInicio.html", {'encuestaInicio': formulario_encuesta_inicio})

