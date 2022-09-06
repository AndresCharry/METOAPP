from .baseDeDatos import baseDeDatos
from .conversor import geo_to_ECEF, ECEF_to_ENU

def Limite_coordenadas(datos):
    datoss = {}
    x_list = []
    y_list = []
    z_list = []
    magnitud = []

    for i in range(0,4):
        if(datos['Coordenadas del campo(latitud)'][i] == min(datos['Coordenadas del campo(latitud)'])):
            minimo = i
            referencia = dict(latitud = datos['Coordenadas del campo(latitud)'][i], longitud = datos['Coordenadas del campo(longitud)'][i], altura = datos['Coordenadas del campo(altura)'][i])
            baseDeDatos.coordenadas_referencia(referencia)
            break
    for i in range(0, 4):
        X,Y,Z = geo_to_ECEF(datos['Coordenadas del campo(latitud)'][i],datos['Coordenadas del campo(longitud)'][i],datos['Coordenadas del campo(altura)'][i])
        x,y,z = ECEF_to_ENU(datos['Coordenadas del campo(latitud)'][minimo],datos['Coordenadas del campo(longitud)'][minimo],datos['Coordenadas del campo(altura)'][minimo],
                                      X, Y , Z)
        x_list.append(abs(x))
        y_list.append(abs(y))
        z_list.append(abs(z))
        numero = ((x**2)+(y**2))**0.5
        magnitud.append(numero)

    indes = magnitud.index(max(magnitud))
    datoss['x'] = x_list[indes]
    datoss['y'] = y_list[indes]
    datoss['z'] = z_list[indes]
    area = round(datoss['x'] * datoss['y'],2)
    datos['Area del cultivo'] = area
    baseDeDatos.datoss(datoss)
    baseDeDatos.datos(datos)