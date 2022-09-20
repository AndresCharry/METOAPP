import pandas as pd


def base_de_datos(url_coordenadas, datos):
    coordenadas = pd.read_csv(url_coordenadas)
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url1 = url.at[0,'url']
    url2 = url.at[0,'Dia de la plantacion']
    text = open(url2 + 'Dia de la plantacion.txt', 'r')
    string = text.read()
    text.close()
    datos['Dia de la plantacion'] = string
    datos[''] = ''
    datos = pd.DataFrame(datos, index = [0])
    coordenadas = pd.concat([datos,coordenadas], axis = 1)
    pandas = pd.read_csv(url1)
    try:
        if pandas.at[0, 'Tipo de cultivo'] != None:
            pandas['Tipo de cultivo'] = coordenadas['Tipo de cultivo']
            pandas['Dia de la plantacion'] = coordenadas['Dia de la plantacion']
            pandas[''] = coordenadas['']
            pandas['Coordenadas del campo(latitud)'] = coordenadas['Coordenadas del campo(latitud)']
            pandas['Coordenadas del campo(longitud)'] = coordenadas['Coordenadas del campo(longitud)']
            pandas['Coordenadas del campo(altura)'] = coordenadas['Coordenadas del campo(altura)']
            pandas.to_csv(url1,index=False, header = True)
    except:
        result = pd.concat([pandas, coordenadas], axis=1)
        result.to_csv(url1,index=False, header = True)
