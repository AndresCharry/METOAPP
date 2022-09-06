import pandas as pd

def datos():
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    try:
        distancia_de_surco = df.at[0, 'Distancia de surco']
        numero_de_surcos = df.at[0, 'Numero de surcos']
        ancho_de_la_hilera = df.at[0, 'Ancho de la hilera']
        Numero_de_arboles_por_hilera = df.at[0, 'Numero de arboles por hilera']
        Distancia_entre_arboles_por_hilera =  df.at[0, 'Distancia entre arboles por hilera']
    except:
        distancia_de_surco = 1
        numero_de_surcos = 1
        ancho_de_la_hilera = 1
        Numero_de_arboles_por_hilera = 1
        Distancia_entre_arboles_por_hilera = 1
        

    return distancia_de_surco, numero_de_surcos, ancho_de_la_hilera, Numero_de_arboles_por_hilera, Distancia_entre_arboles_por_hilera