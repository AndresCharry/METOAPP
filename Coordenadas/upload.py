import pandas as pd

def handle_uploaded_file(f):
    url = '/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Coordenadas/baseDeDatos/coordenadas_csv/'+f.name
    with open(url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    url2 = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url2 = url2.at[0,'Dia de la plantacion']
    text = open( url2 + 'numero de zonas.txt','r')
    num = text.read()
    num = int(num)
    text.close()

    latitud = []
    longitud = []
    url1 = pd.read_csv(url)
    for num in range (num + 1):
        latitud.append(url1[f'zona{num} (latitud)'].values.tolist())
        longitud.append(url1[f'zona{num} (longitud)'].values.tolist())

    return url, latitud, longitud, num
