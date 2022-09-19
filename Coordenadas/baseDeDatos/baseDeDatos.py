import pandas as pd


def base_de_datos(url_coordenadas):
    coordenadas = pd.read_csv(url_coordenadas)
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url = url.at[0,'url']
    pandas = pd.read_csv(url)
    try:
        if pandas.at[0, 'Coordenadas del campo(latitud)'] != None:
            pandas['Coordenadas del campo(latitud)'] = coordenadas['Coordenadas del campo(latitud)']
            pandas['Coordenadas del campo(longitud)'] = coordenadas['Coordenadas del campo(longitud)']
            pandas['Coordenadas del campo(altura)'] = coordenadas['Coordenadas del campo(altura)']
            pandas.to_csv(url,index=False, header = True)
    except:
        result = pd.concat([pandas, coordenadas], axis=1)
        result.to_csv(url,index=False, header = True)

        
def datoss(datoss):
    df = pd.DataFrame(datoss, index = [0])
    df.to_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Coordenadas/baseDeDatos/coordenadas_csv/coordenasxyz.csv',header= True, index=False)

def coordenadas_referencia(referencia):
    df = pd.DataFrame(referencia, index=[0])
    df.to_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Coordenadas/baseDeDatos/coordenadas_csv/coordenasReferencia.csv',header= True, index=False)
