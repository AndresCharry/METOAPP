import pandas as pd


def datos(datos):
    df = pd.DataFrame(datos,index=[0])
    df.to_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/Variables.csv',
                header= True, index=False)

    return df

def base_arboles(datos,num):
    datos[''] = ' '
    datos = pd.DataFrame(datos)
    datos.to_csv(f'/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/arboles_csv/arbol{num}.csv',
                            header= True, index=False)

def base_arbol(datos):
    datos[''] = ''
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    pandas = pd.read_csv(url)
    datos = pd.DataFrame(datos)
    try:
        for key in datos.keys():
            if key != '':
                if pandas.at[0, key] != None:
                    pandas[key] = datos[key]
                    pandas.to_csv(url,index=False, header = True)
    except:
        result = pd.concat([pandas,datos], axis=1)
        result.to_csv(url,index=False, header = True)

def scan_lidar():
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    lidar = pd.read_csv(url)
    lidar = lidar['lidar'][0]

    return lidar

def lista_puntos_marcadores():
    puntos = []
    marcadores = []
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url, header = True)
    puntos = [df['puntos latitud'],df['puntos longitud']]
    marcadores = [df['marcadores latitud'], df['marcadores longitud']]
    return puntos, marcadores
