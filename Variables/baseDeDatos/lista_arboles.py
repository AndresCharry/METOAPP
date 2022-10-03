import pandas as pd
from Coordenadas.conversor import ENU_TO_ECEF, ECEF_to_geo

def datos():
    latitud = []
    longitud = []
    lista = []
    diccionario  = {}
    df = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/arboles_xy.csv',)
    arboles = df.to_dict('list')
    df = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Coordenadas/baseDeDatos/coordenadas_csv/coordenasReferencia.csv', header=0)

    for i  in range(0,len(arboles['arboles_escogidos_x'])):
        X,Y,Z = ENU_TO_ECEF(df['latitud'], df['longitud'], df['altura'], arboles['arboles_escogidos_x'][i], arboles['arboles_escogidos_y'][i], 0)
        lat,log,H = ECEF_to_geo(X, Y, Z) 
        latitud.append(lat)
        longitud.append(log)
        lista.append([lat,log])

    diccionario = {'Coordenadas de los puntos (latitud)': latitud, 'Coordenadas de los puntos (longitud)' : longitud, '':'' }
    datos = pd.DataFrame(diccionario)
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    pandas = pd.read_csv(url)
    try:
        if pandas.at[0, 'Coordenadas de los puntos (latitud)'] != None:
            pandas['Coordenadas de los puntos (latitud)'] = datos['Coordenadas de los puntos (latitud)']
            pandas['Coordenadas de los puntos (longitud)'] = datos['Coordenadas de los puntos (longitud)']
            pandas.to_csv(url,index=False, header = True)
    except:
        result = pd.concat([pandas,datos], axis=1)
        result.to_csv(url,index=False, header = True)


def lista():
    listas = []
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/arboles_xy.csv')
    for x in range(0,len(url['puntos (latitud)'].values)):
        listas.append([round(url.at[x, 'puntos (latitud)'],6),round(url.at[x, 'puntos (longitud)'],6)])
    
    return listas
