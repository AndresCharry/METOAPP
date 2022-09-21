import pandas as pd

def datos():
    df = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Coordenadas/baseDeDatos/coordenadas_csv/coordenasxyz.csv', header=0)
    diccionario = {}
    diccionario = {'x': df['x'], 'y': df['y']}
    return diccionario
