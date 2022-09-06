from django.shortcuts import render
from ModeloLidar.baseDeDatos import BaseDeDatos

def VistaModelo(request):
    resultados = BaseDeDatos.Datos_lidar()
    diccionario = {}
    cantidad_de_escaneos = int(resultados['cantidad de escaneos'])
    resolucion = round(float(resultados['resolucion']),2)
    distancia_promedio = round(float(resultados['distancia promedio']),2)
    angulo_incidencia = round(float(resultados['angulo incidencia']),2)
    diccionario = {'cantidad_de_escaneos': cantidad_de_escaneos, 
                   'resolucion': resolucion,
                   'distancia_promedio': distancia_promedio,
                   'angulo_incidencia': angulo_incidencia}

    return render(request, "ModeloLidar/vistaModelo.html",diccionario)