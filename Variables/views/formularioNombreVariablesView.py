from django.shortcuts import render, redirect

from Variables.forms import FormularioNombreVariables
from Variables.baseDeDatos import baseDeDatos, numero_v, arboles_marcadores, x_y, numero_marcadores, variables_modelo, lista_marcadores, lista_arboles
from Variables.sc_surcos import modelo 
from .nombreVariables import NombreVariables
from Encuesta2.baseDeDatos import surcos


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
            datos['numero de puntos a medir'] = request.POST.get("arb_esc")
            num_puntos = int(datos['numero de puntos a medir'])
            baseDeDatos.datos(datos)
            coordenadasXY = x_y.datos()
            numero_de_marcadores = int(numero_marcadores.datos())
            surco = surcos.datos()
            if surco == True:
                surco = 1
            else:
                surco = 0
            
            distancia_de_surco, numero_de_surcos, ancho_de_la_hilera, Numero_de_arboles_por_hilera, Distancia_entre_arboles_por_hilera = variables_modelo.datos()
            # surcos,X_camp, Y_camp, num_markers, arb_esc, vs, n_s, v, num_arb, esp_arb
            arboles_escogidos, marcadores = modelo(surco, int(coordenadasXY['x']), int(coordenadasXY['y']), numero_de_marcadores, num_puntos,
                                                   distancia_de_surco, numero_de_surcos, ancho_de_la_hilera, Numero_de_arboles_por_hilera, Distancia_entre_arboles_por_hilera )
            # arboles_escogidos, marcadores = sin_surcos( int(coordenadasXY['x']), int(coordenadasXY['y']), numero_de_marcadores, int(datos['numero de puntos a medir']))
            arboles_marcadores.datos(arboles_escogidos, marcadores)
            lista_marcadores.datos()
            lista_arboles.datos()
            # arboles_marcadores.convertidor()
            return redirect("/formularioNombreVariables/?valido")

    return render(request, "Variables/nombreVariables.html",formularioNombreVariables )

