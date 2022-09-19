import pandas as pd

def Datos_lidar():
    df = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/ModeloLidar/baseDeDatos/ModeloLidar_csv/ModeloLidar.csv', header=0)
    diccionario = {}
    diccionario = {'Altura del lidar': df['Altura del lidar'],
                   'Angulo del lidar': df['Angulo del lidar'], 
                   'velocidad de la plataforma':df['velocidad de la plataforma'],
                   'Resolucion angular de anillos': df['Resolucion angular de anillos'],
                   'Numero de anillos': df['Numero de anillos']}
    return diccionario
