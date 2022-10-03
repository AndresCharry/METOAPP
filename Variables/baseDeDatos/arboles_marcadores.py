import pandas as pd

def datos(arboles_escogidos):
    df = pd.DataFrame(arboles_escogidos)
    df.to_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Variables/baseDeDatos/Variables_csv/arboles_xy.csv',
                            header= True, index=False)

def convinar(dic):
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url1 = url.at[0,'url']
    baseDatos = pd.read_csv(url1)
    puntos = pd.DataFrame(dic)
    try:
        if baseDatos.at[0, 'Tipo de cultivo'] != None:
            baseDatos['puntos (latitud)'] = puntos['puntos (latitud)']
            baseDatos['puntos (longitud)'] = puntos['puntos (longitud)']
    except:
        final = pd.concat([baseDatos,puntos], axis = 1)
        final.to_csv(url1,index=False, header = True)


