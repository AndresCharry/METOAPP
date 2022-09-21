from django.shortcuts import render, redirect

from Variables.forms import FormularioVariables
from Variables.baseDeDatos import lista_marcadores, lista_arboles, numero_puntos, numero_v, baseDeDatos
from .cuerpo_view import condicion, lectura


# Create your views here.
def Variables(request):
    formulario_variables = FormularioVariables()
    marcadores = lista_marcadores.lista()
    puntos = lista_arboles.lista()
    numero_variables = numero_v.datos()
    num_marcadores = lista_marcadores.numero_marcadores()
    num_puntos = numero_puntos.datos()
    variables = numero_v.num_var()
    nom_var = numero_v.nom_var()
    num = lectura(num_puntos)
    if num != num_puntos:
        num1 = puntos[num]
    else:
        num1 = puntos[-1]
    # lidar = baseDeDatos.scan_lidar()
    
    formularioVariables = {'formularioVariables': formulario_variables,'numero_variables': numero_variables,
                            'variables' : variables, 'puntos':num1 , 'marcadores': marcadores,
                            'num_puntos': num_puntos, 'nom_variables': nom_var, 'num' : num+1, 'lidar': False,
                            'num_marcadores': num_marcadores}

    if request.method == "POST":
        formulario_variables = FormularioVariables(data=request.POST)
        if formulario_variables.is_valid():
            condicion(request, nom_var, num_puntos, numero_variables, variables)
            return redirect("/formularioVariables/?valido")

    return render(request, "Variables/variables.html", formularioVariables )

