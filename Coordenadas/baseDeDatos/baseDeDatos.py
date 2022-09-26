import pandas as pd

def base_de_datos(url_coordenadas, datos, num_zonas, marcadores = None):
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
    if marcadores != None:
        marcadores[''] = ''
        marcadores = pd.DataFrame(marcadores)
        coordenadas = pd.concat([coordenadas,marcadores], axis = 1)
    pandas = pd.read_csv(url1)
    try:
        if pandas.at[0, 'Tipo de cultivo'] != None:
            pandas['Tipo de cultivo'] = coordenadas['Tipo de cultivo']
            pandas['Dia de la plantacion'] = coordenadas['Dia de la plantacion']
            pandas[''] = coordenadas['']
            for num in range(num_zonas):
                pandas[f'zona{num} (latitud)'] = coordenadas[f'zona{num} (latitud)']
                pandas[f'zona{num} (longitud)'] = coordenadas[f'zona{num} (longitud)']
            pandas[''] = ''
            if marcadores != None:
                pandas['marcadores (latitud)'] = coordenadas['marcadores (latitud)']
                pandas['marcadores (longitud)'] = coordenadas['marcadores (longitud)']
            pandas.to_csv(url1,index=False, header = True)
    except:
        result = pd.concat([pandas, coordenadas], axis=1)
        result.to_csv(url1,index=False, header = True)
