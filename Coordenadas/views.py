from Variables.baseDeDatos.lista_marcadores import numero_marcadores
from django.shortcuts import render, redirect
import pandas as pd

from .forms import FormularioCoordenadas
from .upload import  handle_uploaded_file
from .baseDeDatos.baseDeDatos import  base_de_datos, maximos
from .final import main 
# Create your views here.

def coordenadas(request):
    formulario_coordenadas = FormularioCoordenadas()
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    try:
        medicion_manual = df.at[0,'Medicion manual']
        print(medicion_manual)
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
                marcadores = int(datos['Numero de marcadores'])
                sensor = 1
                marcadores_l, marcadores_lg, x_max, y_max = main(num_zonas_en_campo = num_zonas,latitud = latitud, longitud = longitud, dron = sensor, num_markers = marcadores) 
                x = x_max
                y = y_max
                marcadores = {
                    "" : "",
                    "Marcadores (latitud)": marcadores_l,
                    "Marcadores (longitud)": marcadores_lg,
                }
                base_de_datos(url_coordenadas, datos, num_zonas, marcadores)
                maximos(x_max,y_max)
            else:
                datos['Numero de variables'] = request.POST.get("n_variables")
                base_de_datos(url_coordenadas, datos, num_zonas)
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
    try:
        dron = df.at[0,'Medicion con dron']
    except:
        dron = False
    lista = [] 
    num = num_marcadores * num_zonas
    for i in range(num):
        lista.append([marcadores_l[i],marcadores_lg[i]])
    print(dron)
    diccionario = {
        'lista': lista,
        'dron': dron, 
    }
    return render(request, "Coordenadas/vista.html", diccionario)
