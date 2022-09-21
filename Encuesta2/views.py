from django.shortcuts import render, redirect

from .forms import SCSurcos
from .baseDeDatos import baseDeDatos
from .baseDeDatos import surcos
import pandas as pd

# Create your views here.

def encuesta2(request):
    formulario_encuesta2 = SCSurcos()
    surco = surcos.datos()
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    area = df.at[0,'Area del cultivo']
    encuesta = {'encuesta2': formulario_encuesta2, 'surcos':surco, 'area': area}
    if request.method == "POST":
        formulario_encuesta2 = SCSurcos(data=request.POST)

        if formulario_encuesta2.is_valid():
            # creaccion del diccionario
            datos= {}
            #if dron == True:
                # pass
            #if lidar == True:
                # pass
            if surco == True:
                datos['Distancia de surco'] = request.POST.get("vs")
                datos['Numero de surcos'] = request.POST.get("n_s")
                datos['Ancho de la hilera'] = request.POST.get("v")
                datos['Numero de arboles por hilera'] = request.POST.get("num_arb")
                datos['Distancia entre arboles por hilera'] = request.POST.get("esp_arb")
                datos['numero de marcadores'] = request.POST.get("numero_de_marcadores")
                datos['numero de variables'] = request.POST.get("n_variables")
                baseDeDatos.datos(datos,surco)
            else:
                datos['numero de marcadores'] = request.POST.get("numero_de_marcadores")
                datos['numero de variables'] = request.POST.get("n_variables")
                baseDeDatos.datos(datos, surco)

            return redirect("/encuesta2/?valido")

    return render(request, "Encuesta2/encuesta2.html", encuesta)
