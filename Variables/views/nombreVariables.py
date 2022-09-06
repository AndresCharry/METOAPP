def NombreVariables(request, numero_variables, datos):
    numero_var = 1
    while numero_var <= numero_variables:
        datos[f'variable{numero_var}'] = request.POST.get(f"variable{numero_var}")
        datos[f'num_variable{numero_var}'] = request.POST.get(f"num_variable{numero_var}")
        numero_var += 1
    
    return datos
