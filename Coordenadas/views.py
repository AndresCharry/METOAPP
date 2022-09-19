from django.shortcuts import render, redirect

from .forms import FormularioCoordenadas
from .upload import  handle_uploaded_file
from .baseDeDatos.baseDeDatos import  base_de_datos
# Create your views here.

def coordenadas(request):
    formulario_coordenadas = FormularioCoordenadas()

    if request.method == "POST":
        formulario_coordenadas = FormularioCoordenadas(request.POST,request.FILES)

        if formulario_coordenadas.is_valid():
            # creaccion del diccionario
            datos = {}
            datos['Tipo de cultivo'] = request.POST.get("tipo_cultivo")
            url_coordenadas = handle_uploaded_file(request.FILES['file'])
            base_de_datos(url_coordenadas)
            return redirect("/coordenadas/?valido")

    return render(request, "Coordenadas/coordenadas.html", {'coordenadas': formulario_coordenadas})

