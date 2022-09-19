from django.http import FileResponse
import pandas as pd


# Create your views here.

def Finalizar(response):
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    response = FileResponse(open(url, 'rb'), as_attachment=True) # with other applicable parameters
    return response

def FinalizarBaseDeDatos(response):
    url1 = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/direccionBaseDatos.csv')
    url1 = url1.at[0,'url']
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/nombreProyecto.csv')
    url2 = url.at[0,'Nombre Proyecto']
    url3 = url.at[0,'Nombre campaña']
    url4 = url.at[0,'Fecha']
    url = url1 + f'{url2}/{url3}/{url4}.csv'
    response = FileResponse(open(url, 'rb'), as_attachment=True) # with other applicable parameters
    return response
