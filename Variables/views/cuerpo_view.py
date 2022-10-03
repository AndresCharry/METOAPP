from Variables.baseDeDatos.baseDeDatos import base_arboles, base_arbol
import os
import glob
import pathlib
import pandas as pd

def condicion(request, nom_var, numero_variables, variables):
    initial_count = 0
    cantidad_variable = 1
    cantidad_datos = 1
    var = []

    for path in pathlib.Path('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/arboles_csv').iterdir():
        if path.is_file():
            initial_count += 1

    punto = initial_count + 1
    datos = {}
    numero = {}
    while cantidad_variable <= numero_variables:
        num = variables[f'num_variable{cantidad_variable}']
        while cantidad_datos <= num:
            numero['numero'] = request.POST.get(f"var{cantidad_variable}_{cantidad_datos}")
            var.append(float(numero['numero']))
            cantidad_datos += 1
        datos[f"Arbol {punto} " + nom_var[f"variable{cantidad_variable}"]] = pd.Series(var)
        cantidad_datos = 1
        cantidad_variable += 1
    base_arboles(datos,punto)
    text = open('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/numero_arboles.txt','w')
    text.write(f'{punto}')
    text.close()
    base_arbol(datos)


def lectura(puntos):
    try:
        text = open('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/numero_arboles.txt','r')
        num = text.read()
        num = int(num)
        text.close()
        if num >= puntos:
            py_files = glob.glob('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/arboles_csv/*.csv')
            text = open('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/numero_arboles.txt','w')
            text.write(f'{0}')
            text.close()
            for py_file in py_files:
                try:
                    os.remove(py_file)
                except:
                    pass
    except:
        num = 0
    return  num
