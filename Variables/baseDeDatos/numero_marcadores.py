import pandas as pd

def datos():
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    df = pd.read_csv(url)
    df = df['numero de marcadores'][0]
    return df
