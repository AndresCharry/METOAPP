import pandas as pd


def datos(datos, surco):
    datos[''] = ' '
    datos = pd.DataFrame(datos, index=[0])
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    pandas = pd.read_csv(url)
    try:
        if pandas.at[0, 'Distancia de surco'] != None:
            if surco == True:
                pandas['Distancia de surco'] = datos['Distancia de surco']
                pandas['Numero de surcos'] = datos['Numero de surcos']
                pandas['Ancho de la hilera'] = datos['Ancho de la hilera']
                pandas['Numero de arboles por hilera'] = datos['Numero de arboles por hilera']
                pandas['Distancia entre arboles por hilera'] = datos['Distancia entre arboles por hilera']
                pandas['numero de marcadores'] = datos['numero de marcadores']
                pandas['numero de variables'] = datos['numero de variables']
            else:
                pandas['numero de marcadores'] = datos['numero de marcadores']
                pandas['numero de variables'] = datos['numero de variables']

        pandas.to_csv(url,index=False, header = True)
    except:
        result = pd.concat([pandas,datos], axis=1)
        result.to_csv(url,index=False, header = True)
