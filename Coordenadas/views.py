from django.shortcuts import render, redirect
import pandas as pd

from .forms import FormularioCoordenadas
from .upload import  handle_uploaded_file
from .baseDeDatos.baseDeDatos import  base_de_datos
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
            datos['Tipo de cultivo'] = request.POST.get("tipo_cultivo")
            if medicion_manual != True:
                datos['Numero de marcadores'] = request.POST.get("numero_de_marcadores")
            else:
                datos['Numero de variables'] = request.POST.get("n_variables")
            url_coordenadas = handle_uploaded_file(request.FILES['file'])
            base_de_datos(url_coordenadas, datos)
            return redirect("/coordenadas/?valido")

    return render(request, "Coordenadas/coordenadas.html", {'coordenadas': formulario_coordenadas, 'manual': medicion_manual})


def vista(request):

    return render(request, "Coordenadas/vista.html")
