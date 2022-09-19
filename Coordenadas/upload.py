def handle_uploaded_file(f):
    with open('/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/Coordenadas/baseDeDatos/coordenadas_csv/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
