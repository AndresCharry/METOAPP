import pandas as pd

def datos():
    df = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/Variables.csv', header= 0)
    diccionario = int(df['numero de puntos a medir'])
    return diccionario