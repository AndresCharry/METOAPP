
from django.shortcuts import render, redirect

from ModeloLidar.forms import FormularioModelo2
from ModeloLidar.baseDeDatos import BaseDeDatos,datos_lidar
from ModeloLidar.modeloLidar import simulacion
from .anillos import Anillos
from Encuesta2.baseDeDatos import surcos

import pandas as pd

# Create your views here.


def formularioModelo2(request):
    formulario_modelo_lidar = FormularioModelo2()
    datos= {}
    datos = datos_lidar.Datos_lidar()
    num_anillos = int(datos['Numero de anillos'][0])
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    furrows = surcos.datos()
    if furrows == True :
        dato = {'dis_furrows': df.at[0,'Distancia de surco']}
    else:
        dato = 0
    diccionario = {'formularioModelo': formulario_modelo_lidar,
                    'anillos': num_anillos}
    if request.method == "POST":
        formulario_modelo_lidar = FormularioModelo2(data=request.POST)

        if formulario_modelo_lidar.is_valid():
            datos = Anillos(request, datos, num_anillos)
            BaseDeDatos.datoss(datos, num_anillos)
            resultados = simulacion(datos,dato)
            BaseDeDatos.Resultados(resultados)
            return redirect("/formularioModelo2/?valido")

    return render(request, "ModeloLidar/formularioModelo2.html", diccionario)


