import pandas as pd

def datos(urls, datos):
    d = dict(url = urls + datos['Fecha'] + '.csv' )
    d1 = {'Dia de la plantacion' : urls }
    df1 = pd.DataFrame(d1 , index = [0])
    df = pd.DataFrame(d , index = [0])
    result = pd.concat([df,df1], axis= 1)
    result.to_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv', header= True, index = False)

def tipo_de_proyecto(datos):
    dato = {}

    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url1 = url.at[0,'url']
    for key in datos.keys():
        if datos[key] == 'on':
            dato = {key: True}
            dato[''] = ''
            break
    df = pd.DataFrame(dato,index=[0])
    df.to_csv(url1, header = True, index = False)

def nombreProyecto(datos):
    df  = pd.DataFrame(datos, index=[0])
    df.to_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/nombreProyecto.csv', header= True, index = False)

def diaPlantacion(dato,url):
    text = open( url + 'Dia de la plantacion.txt','w')
    text.write(f'{dato["Dia de la plantacion"]}')
    text.close()
    
def zonas_cultivo(dato, url):
    text = open( url + 'numero de zonas.txt','w')
    text.write(f'{dato["zona"]}')
    text.close()
