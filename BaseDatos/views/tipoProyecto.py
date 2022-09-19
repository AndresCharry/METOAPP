from django.shortcuts import render, redirect

from BaseDatos.forms import TipoProyecto
from BaseDatos.BaseDeDatos.baseDatos import tipo_de_proyecto
# Create your views here.

def TipoDeProyecto(request):
    formulario_tipo_proyecto = TipoProyecto()
    diccionario = {}
    diccionario = {'formulario':formulario_tipo_proyecto}

    if request.method == "POST":
        formulario_tipo_proyecto = TipoProyecto(data=request.POST)

        if formulario_tipo_proyecto.is_valid():
            # creaccion del diccionario
            datos= {}
            datos['Medicion manual'] = request.POST.get("medicion")
            datos['Medicion con dron'] = request.POST.get("dron")
            datos['Medicion con LiDAR'] = request.POST.get("lidar")
            tipo_de_proyecto(datos)
            return redirect("/tipoProyecto/?valido")


    return render(request, "BaseDatos/tipoDeProyecto.html", diccionario)
