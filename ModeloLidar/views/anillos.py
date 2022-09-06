def Anillos(request, datos, anillos):
    anillo = 1
    ring = []
    while anillo <= anillos:
        ring.append(request.POST.get(f"anillo{anillo}"))
        anillo += 1
    datos['angulos_lidar'] = ring

    return datos