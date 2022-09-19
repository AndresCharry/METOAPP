import pandas as pd
from Coordenadas.conversor import ENU_TO_ECEF, ECEF_to_geo

def datos(arboles_escogidos, marcadores__escogidos):
    df = pd.DataFrame(arboles_escogidos)
    df.to_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/arboles_xy.csv',
                            header= True, index=False)
    df = pd.DataFrame(marcadores__escogidos)
    df.to_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/marcadores_xy.csv',
                            header= True, index=False)

