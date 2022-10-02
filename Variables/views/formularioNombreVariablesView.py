from django.shortcuts import render, redirect

from Variables.forms import FormularioNombreVariables
from Variables.baseDeDatos import baseDeDatos, numero_v, arboles_marcadores
from .nombreVariables import NombreVariables
import pandas as pd
from Coordenadas.final import main



# Create your views here.
def nombreVariables(request):
    formulario_nombre_variables = FormularioNombreVariables()
    datos= {}
    numero_variables = numero_v.datos()
    formularioNombreVariables = {'formularioNombreVariables': formulario_nombre_variables,'num': numero_variables}
    if request.method == "POST":
        formulario_nombre_variables = FormularioNombreVariables(data=request.POST)
        if formulario_nombre_variables.is_valid():
            datos = NombreVariables(request, numero_variables, datos)
            datos['numero de puntos a medir por zona'] = request.POST.get("arb_esc")
            datos['puntos por hectaria'] = request.POST.get("hectarias")
            num_puntos = int(datos['numero de puntos a medir por zona'])
            hectaria = int(datos['puntos por hectaria'])
            url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
            url2 = url.at[0,'Dia de la plantacion']
            text = open( url2 + 'numero de zonas.txt','r')
            num = text.read()
            text.close()
            num_zonas = int(num)
            datos['puntos totales'] = num_puntos * num_zonas
            latitud = []
            longitud = []
            url1 = url.at[0,'url']
            pandas = pd.read_csv(url1) 
            for num in range (num_zonas + 1):
                latitud.append(pandas[f'zona{num} (latitud)'].values.tolist())
                longitud.append(pandas[f'zona{num} (longitud)'].values.tolist())
         
            baseDeDatos.datos(datos)
            
            # ToDo: cuadrar el programa de juan
            puntos_l, puntos_lg = main(num_zonas_en_campo = num_zonas, latitud = latitud, longitud = longitud, puntos_por_area = num_puntos, pph = hectaria) 
            dic ={
                '': '', 
                'puntos (latitud)': puntos_l,
                'puntos (longitud)': puntos_lg
            }

            arboles_marcadores.datos(dic)
            arboles_marcadores.convinar(dic)
            return redirect("/formularioNombreVariables/?valido")

    return render(request, "Variables/nombreVariables.html",formularioNombreVariables )

