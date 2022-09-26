from django.shortcuts import render, redirect
import pandas as pd

from .forms import FormularioCoordenadas
from .upload import  handle_uploaded_file
from .baseDeDatos.baseDeDatos import  base_de_datos
from .copia_de_copia_de_listo import main 
# Create your views here.

def coordenadas(request):
    formulario_coordenadas = FormularioCoordenadas()
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    try:
        medicion_manual = df.at[0,'Medicion manual']
    except:
        medicion_manual = False
 
    if request.method == "POST":
        formulario_coordenadas = FormularioCoordenadas(request.POST,request.FILES)
        if formulario_coordenadas.is_valid():
            # creaccion del diccionario
            datos = {}
            marcadores = {}
            datos['Tipo de cultivo'] = request.POST.get("tipo_cultivo")
            url_coordenadas, latitud, longitud, num_zonas = handle_uploaded_file(request.FILES['file'])
            num_zonas = int(num_zonas)
            if medicion_manual != True:
                datos['Numero de zonas del cultivo'] =  num_zonas
                datos['Numero de marcadores'] = request.POST.get("numero_de_marcadores")
                datos['Distancia entre marcadores'] = request.POST.get("hectarias")
                marcadores = int(datos['Numero de marcadores'])
                hectarias = int(datos['Distancia entre marcadores'])
                marcadores_l, marcadores_lg = main(num_zonas, marcadores, hectarias, latitud, longitud) 
                marcadores = {
                    "" : "",
                    "Marcadores (latitud)": marcadores_l,
                    "Marcadores (longitud)": marcadores_lg,
                }
            else:
                datos['Numero de variables'] = request.POST.get("n_variables")
            base_de_datos(url_coordenadas, datos, num_zonas, marcadores)
            return redirect("/coordenadas/?valido")

    return render(request, "Coordenadas/coordenadas.html", {'coordenadas': formulario_coordenadas, 'manual': medicion_manual})


def vista(request):
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    marcadores_l = df['Marcadores (latitud)'].values.tolist()
    marcadores_lg = df['Marcadores (longitud)'].values.tolist()
    num_marcadores = int(df.at[0,'Numero de marcadores'])
    num_zonas = int(df.at[0, 'Numero de zonas del cultivo']) 
    lista = range(num_marcadores * num_zonas)
    diccionario = {
        'marcadores(latitud)': marcadores_l,
        'marcadores(longitud)': marcadores_lg,
        'lista': lista,
    }
    return render(request, "Coordenadas/vista.html", diccionario)
