from django.shortcuts import render, redirect

from .forms import FormularioCoordenadas
from .upload import  handle_uploaded_file
from .baseDeDatos.baseDeDatos import datos 
# Create your views here.

def coordenadas(request):
    formulario_coordenadas = FormularioCoordenadas()

    if request.method == "POST":
        formulario_coordenadas = FormularioCoordenadas(request.FILES)

        print(formulario_coordenadas.is_valid())
        if formulario_coordenadas.is_valid():
            print(1)
            # creaccion del diccionario
            url_coordenadas = handle_uploaded_file(request.FILES['file'])
            datos(url_coordenadas)
            return redirect("/coordenadas/?valido")

    return render(request, "Coordenadas/coordenadas.html", {'coordenadas': formulario_coordenadas})

