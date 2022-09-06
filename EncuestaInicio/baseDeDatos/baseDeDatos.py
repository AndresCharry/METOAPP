import string
import pandas as pd

def datos(datos):
    url = pd.read_csv('/home/andres/Documentos/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url1 = url.at[0,'url']
    url2 = url.at[0,'Dia de la plantacion']
    text = open( url2 +'Dia de la plantacion.txt','r')
    string = text.read()
    text.close()
    datos['Dia de la plantacion'] = string
    datos[''] = ''
    df = pd.DataFrame(datos,index=[0])
    df.to_csv(url1,header= True, index=False)

    return df