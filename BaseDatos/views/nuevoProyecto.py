from django.shortcuts import render,redirect

from BaseDatos.forms import Proyecto, campañas, Fechas
from BaseDatos.BaseDeDatos import baseDatos
from pathlib import Path
import pandas as pd
# Create your views here.

def NuevoProyecto(request):
   
    formulario_nuevo_proyecto = Proyecto()
    diccionario = {'formulario_proyecto':formulario_nuevo_proyecto }
    if request.method == "POST":
        formulario_nuevo_proyecto = Proyecto(data=request.POST)

        if formulario_nuevo_proyecto.is_valid():
            datos= {}
            dato= {}
            datos['nombre del proyecto'] = request.POST.get("nombre_proyecto")
            datos['Nombre de la campaña'] = request.POST.get("nombre_campaña")
            dato['Dia de la plantacion'] = request.POST.get("dia_plantacion")
            datos['Fecha'] = request.POST.get("fecha")
            try:
                url = f'/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/Base_datos/{datos["nombre del proyecto"]}/{datos["Nombre de la campaña"]}/'
                path = Path(url)
                path.mkdir(parents=True)
            except:
                pass
            baseDatos.datos(url, datos)
            baseDatos.diaPlantacion(dato, url)
            return redirect("/nuevoProyecto/?valido")

    return render(request, "BaseDatos/nuevoProyecto.html", diccionario)

def NuevoProyecto2(request):
   
    formulario_nuevo_proyecto = campañas()
    url2 = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/nombreProyecto.csv')
    url2 = url2.at[0,'Nombre Proyecto']
    diccionario = {'formulario_proyecto':formulario_nuevo_proyecto , 'proyecto': url2}
    if request.method == "POST":
        formulario_nuevo_proyecto = campañas(data=request.POST)

        if formulario_nuevo_proyecto.is_valid():
            datos= {}
            dato= {}
            datos['nombre del proyecto'] = url2
            datos['Nombre de la campaña'] = request.POST.get("nombre_campaña")
            dato['Dia de la plantacion'] = request.POST.get("dia_plantacion")
            datos['Fecha'] = request.POST.get("fecha")
            try:
                url = f'/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/Base_datos/{datos["nombre del proyecto"]}/{datos["Nombre de la campaña"]}/'
                path = Path(url)
                path.mkdir(parents=True)
            except:
                pass
            baseDatos.datos(url, datos)
            baseDatos.diaPlantacion(dato, url)
            return redirect("/nuevoProyecto/?valido")

    return render(request, "BaseDatos/nuevoProyecto2.html", diccionario)

def NuevoProyecto3(request):
   
    formulario_nuevo_proyecto = Fechas()
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/nombreProyecto.csv')
    url2 = url.at[0,'Nombre Proyecto']
    url3 = url.at[0,'Nombre campaña']
    diccionario = {'formulario_proyecto':formulario_nuevo_proyecto,'proyecto':url2,'campaña':url3 }
    if request.method == "POST":
        formulario_nuevo_proyecto = Fechas(data=request.POST)

        if formulario_nuevo_proyecto.is_valid():
            datos= {}
            datos['nombre del proyecto'] = url2
            datos['Nombre de la campaña'] = url3
            datos['Fecha'] = request.POST.get("fecha")
            try:
                url = f'/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/Base_datos/{datos["nombre del proyecto"]}/{datos["Nombre de la campaña"]}/'
                path = Path(url)
                path.mkdir(parents=True)
            except:
                pass
            baseDatos.datos(url, datos)
            return redirect("/nuevoProyecto/?valido")

    return render(request, "BaseDatos/nuevoProyecto3.html", diccionario)
