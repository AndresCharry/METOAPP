from django.shortcuts import render, redirect

from .forms import FormularioCoordenadas
from .limites_coordenadas import Limite_coordenadas
# Create your views here.


def coordenadas(request):
    formulario_coordenadas = FormularioCoordenadas()

    if request.method == "POST":
        formulario_coordenadas = FormularioCoordenadas(data=request.POST)

        if formulario_coordenadas.is_valid():
            # creaccion del diccionario
            datos = {}
            datos['Coordenadas del campo(latitud)'] = [request.POST.get("lat_1"),request.POST.get("lat_2"),request.POST.get("lat_3"),request.POST.get("lat_4")]
            datos['Coordenadas del campo(longitud)'] = [request.POST.get("log_1"),request.POST.get("log_2"),request.POST.get("log_3"),request.POST.get("log_4")]
            datos['Coordenadas del campo(altura)'] = [request.POST.get("h1"),request.POST.get("h2"),request.POST.get("h3"),request.POST.get("h4")]
            Limite_coordenadas(datos)
            return redirect("/coordenadas/?valido")

    return render(request, "Coordenadas/coordenadas.html", {'coordenadas': formulario_coordenadas})
