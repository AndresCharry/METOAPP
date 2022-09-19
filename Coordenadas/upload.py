def handle_uploaded_file(f):
    url = '/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Coordenadas/baseDeDatos/coordenadas_csv/'+f.name
    with open(url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return url
