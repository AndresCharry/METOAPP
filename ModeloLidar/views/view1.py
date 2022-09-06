from django.shortcuts import render, redirect

from ModeloLidar.forms import FormularioModelo
from ModeloLidar.baseDeDatos import BaseDeDatos

# Create your views here.


def formularioModelo(request):
    formulario_modelo_lidar = FormularioModelo()

    if request.method == "POST":
        formulario_modelo_lidar = FormularioModelo(data=request.POST)

        if formulario_modelo_lidar.is_valid():
            # creaccion del diccionario
            datos= {}
            datos['Altura del lidar'] = request.POST.get("tZ")
            datos['Angulo del lidar'] = request.POST.get("alpha")
            datos['velocidad de la plataforma'] = request.POST.get("platform_speed")
            datos['Resolucion angular de anillos'] = request.POST.get("angular_ring_resolution")
            datos['Numero de anillos'] = request.POST.get("numero_anillos")
            BaseDeDatos.datos(datos)
            return redirect("/formularioModelo/?valido")

    return render(request, "ModeloLidar/formularioModelo.html", {'formularioModelo': formulario_modelo_lidar})


