from email import header
import pandas as pd

def datos(datos):
    df = pd.DataFrame(datos,index=[0])
    df.to_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/ModeloLidar/baseDeDatos/ModeloLidar_csv/ModeloLidar.csv',
                header= True, index=False)

def datoss(datos, indes):
    datos[''] = ''
    indes = range(0,indes)
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    datos = pd.DataFrame(datos, index = indes)
    try:
        if df.at[0, 'angulos_lidar'] != None:
            df['angulos_lidar'] = datos['angulos_lidar']
            df.to_csv(url,index=False, header = True)
    except:
        result = pd.concat([df,datos], axis=1)
        result.to_csv(url,index=False, header = True)


def Resultados(datos):
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    datos = pd.DataFrame(datos, index = [0])
    result = pd.concat([df,datos], axis=1)
    result.to_csv(url,index=False, header = True)

 
def Datos_lidar():
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    diccionario = {}
    diccionario = {'cantidad de escaneos': df.at[0,'cantidad de escaneos'],
                   'resolucion': df.at[0,'resolucion'], 
                   'distancia promedio':df.at[0,'distancia promedio'],
                   'angulo incidencia': df.at[0,'angulo incidencia']}
    return diccionario