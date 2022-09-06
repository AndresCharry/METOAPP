from django.shortcuts import render,redirect

from BaseDatos.BaseDeDatos.baseDatos import nombreProyecto
from BaseDatos.forms import Fecha, NombreProyecto, NombreCampaña
import pandas as pd
import os
# Create your views here.

def BaseDatos(request):
    formulario_nombre_proyecto = NombreProyecto()
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/direccionBaseDatos.csv')
    url = url.at[0,'url']
    lista = os.listdir(url)
    diccionario = {}
    diccionario = {'formulario':formulario_nombre_proyecto, 'lista':lista}
    
    if request.method == "POST":
        formulario_nombre_proyecto = NombreProyecto(data=request.POST)

        if formulario_nombre_proyecto.is_valid():
            # creaccion del diccionario
            datos= {}
            datos['Nombre Proyecto'] = request.POST.get("nombre_proyecto")
            nombreProyecto(datos)
            return redirect("/baseDatos/?valido")

    return render(request, "BaseDatos/BaseDatos.html",diccionario)


def BaseDatos2(request):
    formulario_nombre_campaña = NombreCampaña()
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/direccionBaseDatos.csv')
    url = url.at[0,'url']
    url2 = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/nombreProyecto.csv')
    url2 = url2.at[0,'Nombre Proyecto']
    lista = os.listdir(url + '/' + url2)
    diccionario = {}
    diccionario = {'formulario':formulario_nombre_campaña, 'lista':lista , 'proyecto': url2}
    
    if request.method == "POST":
        formulario_nombre_campaña = NombreCampaña(data=request.POST)

        if formulario_nombre_campaña.is_valid():
            # creaccion del diccionario
            datos= {}
            datos['Nombre Proyecto'] = url2
            datos['Nombre campaña'] = request.POST.get("nombre_campaña")
            nombreProyecto(datos)
            return redirect("/baseDatos2/?valido")

    return render(request, "BaseDatos/BaseDatos2.html",diccionario)

def BaseDatos3(request):
    formulario_fecha = Fecha()
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/direccionBaseDatos.csv')
    url = url.at[0,'url']
    url2 = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/nombreProyecto.csv')
    url3 = url2.at[0,'Nombre Proyecto']
    url4 = url2.at[0,'Nombre campaña']
    suffix=".csv"
    filenames = os.listdir(url + '/' + url3 + '/' + url4)
    lista = [ filename for filename in filenames if filename.endswith( suffix ) ]
    diccionario = {}
    diccionario = {'formulario':formulario_fecha, 'lista':lista , 'proyecto': url3, 'campaña': url4}
    
    if request.method == "POST":
        formulario_fecha= Fecha(data=request.POST)

        if formulario_fecha.is_valid():
            # creaccion del diccionario
            datos= {}
            datos['Nombre Proyecto'] = url3
            datos['Nombre campaña'] = url4
            datos['Fecha'] = request.POST.get("fecha")
            print(datos)
            nombreProyecto(datos)
            return redirect("/baseDatos3/?valido")

    return render(request, "BaseDatos/BaseDatos3.html",diccionario)
