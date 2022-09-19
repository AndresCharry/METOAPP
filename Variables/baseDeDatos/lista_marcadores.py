import pandas as pd
from Coordenadas.conversor import ENU_TO_ECEF, ECEF_to_geo

def datos():
    latitud = []
    longitud = []
    lista = []
    diccionario = {}
    df = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/marcadores_xy.csv',)
    marcadores = df.to_dict('list')
    df = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Coordenadas/baseDeDatos/coordenadas_csv/coordenasReferencia.csv', header=0)

    for i  in range(0,len(marcadores['marcadores_x'])):
        X,Y,Z = ENU_TO_ECEF(df['latitud'], df['longitud'], df['altura'], marcadores['marcadores_x'][i], marcadores['marcadores_y'][i], 0)
        lat,log,H = ECEF_to_geo(X, Y, Z) 
        latitud.append(lat)
        longitud.append(log)
        lista.append([lat,log])

    diccionario = {'Coordenadas de los marcadores (latitud)' : latitud, 'Coordenadas de los marcadores (longitud)' : longitud, '': ''}
    datos = pd.DataFrame(diccionario)
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    pandas = pd.read_csv(url)
    try:
        if pandas.at[0, 'Coordenadas de los marcadores (latitud)'] != None:
            
            pandas['Coordenadas de los marcadores (latitud)'] = datos['Coordenadas de los marcadores (latitud)']
            pandas['Coordenadas de los marcadores (longitud)'] = datos['Coordenadas de los marcadores (longitud)']
            pandas.to_csv(url,index=False, header = True)
    except:
        result = pd.concat([pandas,datos], axis=1)
        result.to_csv(url,index=False, header = True)


def lista():
    listas = []
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    pandas = pd.read_csv(url)
    for x in range(0,len(pandas['Coordenadas de los marcadores (latitud)'].values)):
        listas.append([round(pandas.at[x, 'Coordenadas de los marcadores (latitud)'],6),round(pandas.at[x, 'Coordenadas de los marcadores (longitud)'],6)])
    
    return listas

def numero_marcadores():
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    df = df.at[0,'numero de marcadores']
    return df
