import pandas as pd

def datos(datos):
    url = pd.read_csv('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/BaseDatos/BaseDeDatos/proyecto.csv')
    url1 = url.at[0,'url']
    url2 = url.at[0,'Dia de la plantacion']
    text = open( url2 +'Dia de la plantacion.txt','r')
    string = text.read()
    text.close()
    datos['Dia de la plantacion'] = string
    datos[''] = ''
    # df = pd.DataFrame(datos,index=[0])
    # df.to_csv(url1,header= True, index=False)
    datos = pd.DataFrame(datos, index=[0])
    pandas = pd.read_csv(url1)
    try:
        if pandas.at[0, 'Dia de la plantacion'] != None:
            pandas['tipo de cultivo'] = datos['tipo de cultivo']
            pandas['surco'] = datos['surco']
            pandas['Dia de la plantacion'] = datos['dia de la plastacion']

        pandas.to_csv(url1,index=False, header = True)
    except:
        result = pd.concat([pandas,datos], axis=1)
        result.to_csv(url1,index=False, header = True)
