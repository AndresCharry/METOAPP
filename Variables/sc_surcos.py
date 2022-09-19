# Librerias__________________________________________________________________________________________________________________
import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt


def modelo(surcos, X_camp, Y_camp, num_markers, arb_esc, vs, n_s, v, num_arb, esp_arb):

    def graficacampo(x, y):
        # Campo______________________________
        # lineas verticales vlines(x,ymin,ymax,'azul')
        ax.vlines(0, 0, y, 'brown')
        ax.hlines(y, 0, x, 'brown')  # lineas horizontales inferiores
        # lineas verticales vlines(x,ymin,ymax,'azul')
        ax.vlines(x, y, 0, 'brown')
        ax.hlines(0, x, 0, 'brown')  # lineas horizontales inferiores

    # VARIABLES DE ENTRADA

    # SURCOS_______________________________________________________________________

    # vs                            # Distancia entre tallo y tallo (surco) en metros
    # v                            # Medida (ancho) de la hilera de cultivo
    # n_s                           # Número de surcos
    # num_arb #esp_arb =            # NÚMERO DE ARBOLES POR HILERA Y ESPACIO ENTRE
    # num_markers                  # NÚMERO DE MARCADORES
    # arb_esc                      # NÚMERO DE ÁRBOLES ESCOGIDO

    # SIN SURCOS___________________________________________________________________

    # X_camp Y_camp                # Dimensiones del campo (x y)
    # num_markers                  # NÚMERO DE MARCADORES
    # arb_esc                      # NÚMERO DE ÁRBOLES ESCOGIDO

    # ELECTOR

    # surcos = 1  # Sí surcos es 0 entonces no hay surcos

    # arb_esc = 1
    num_markers = num_markers - 4

    if surcos == 1:
        # Distancia entre tallo y tallo (surco) en metros INPUT
        vs = float(vs)
        # Número de surcos                                INPUT
        n_s = int(n_s)
        # Medida (ancho) de la hilera de árboles          INPUT
        v = float(v)
        # Número de árboles por hilera                    INPUT
        num_arb = int(num_arb)
        num_total_arboles = num_arb
        arb_y = num_total_arboles
        # Espacio entre plantas en metros                 INPUT
        esp_arb = float(esp_arb)
        r = v/2
        n_v = n_s + 1                                           # Número de vegetación
        s = vs-v                                                # Medida del surco en metros
        xm = s/2
        ym = xm                                       # Margenes
        X_camp = v*n_v+s*n_s
        Y_camp = (v*num_arb + ((num_arb-1)*esp_arb)) + 4 * \
            ym                     # Dimensiones del campo en metros
        print("Cada vegetación mide: ", v)
        print("Distancia en x de tallo a tallo: ", s+v)

    elif surcos == 0:

        X_camp = X_camp
        Y_camp = Y_camp                              # Dimensiones del campo en metros

        arbolesx = []
        arbolesy = []
        num_arb = 0
        arb_y = 0
        arb_x = 0
        arbolitox = []
        arbolitoy = []

        for i in range(0, X_camp+1):
            for j in range(0, Y_camp+1):
                arbolesx.append(i)
                arbolesy.append(j)
                arbolitox.append(i)
                arbolitoy.append(j)
                num_arb += 1

            if i == 0:
                arb_y = num_arb
                arb_x = num_arb

        # Distancia entre tallo y tallo (surco) en metros INPUT
        vs = 2
        n_s = arb_x-1                                           # Número de surcos
        # Medida (ancho) de la hilera de árboles          INPUT
        v = 1
        num_total_arboles = num_arb
        # Número de árboles por hilera                    (INPUT)
        num_arb = arb_y
        num_esp = arb_y-1
        # Espacio entre plantas en metros                 NO
        esp_arb = 1

        n_v = n_s + 1                                           # Número de vegetación
        s = vs-v                                                # Medida del surco en metros
        r = s/3

        xm = s/2
        ym = xm                                       # Margenes
        print("Cada vegetación mide: ", v)
        print("Distancia en x de tallo a tallo: ", s+v)

    lineasv = []
    lineash = []


    # Trayectoria__________________________________________________________________


    def trayects(X_camp, Y_camp, xm, ym):
        # Linea vertical
        if surcos == 1:
            xv = v+xm
        else:
            xv = xm
        yv = 0
        lineasv.append(xv)
        lineash.append(Y_camp-ym)
        if surcos == 1:
            xv = xv+(2*xm)+v
        else:
            xv = xv+v

        arriba = 0

        while ((xv) <= (X_camp)):
            lineasv.append(xv)
            if arriba == 1:
                lineash.append(Y_camp-ym)
                arriba = 0
            else:
                lineash.append(ym)
                arriba = 1
            if surcos == 1:
                xv = xv+(2*xm)+v
            else:
                xv = xv+v

        return lineasv, lineash


    lineas_camp = []                                    # Hileras de los arboles
    x1 = 0
    x2 = x1+v
    y1 = 2*ym
    y2 = Y_camp-y1
    for i in range(n_v):
        lineas_camp.append(x1+(v/2))
        x1 = x1+(v+s)
        x2 = x1+v

    xv = lineas_camp[0]
    yv = 2*ym

    # Hacer los árboles___________________________________________________________


    def arboles(num_total_arboles, r, xv, yv, esp_arb, v):
        yv = yv+v/2
        a = []
        b = []

        theta = np.linspace(0, 2*np.pi, 360)

        for i in range(num_total_arboles):
            a.append(xv)
            b.append(yv)
            yv = yv+(2*r+esp_arb)

        return a, b

    # Funciones___________________________________________________________________


    def es_primo(num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True


    def filas_columnas(number):
        m1 = []
        m2 = []
        for divisor in range(1, number+1):
            if (number % divisor) == 0:
                if (divisor <= h and int(number / divisor) <= l) or (divisor <= l and int(number / divisor) <= h):
                    m1.append(divisor)
                    m2.append(int(number / divisor))
        mm = []
        for i in range(len(m1)):
            mm.append(abs(m1[i]-m2[i]))

        if m1[mm.index(min(mm))] >= m2[mm.index(min(mm))]:    # M1 siempre será el mayor
            mn1 = m1[mm.index(min(mm))]
            mn2 = m2[mm.index(min(mm))]

        else:
            mn1 = m2[mm.index(min(mm))]
            mn2 = m1[mm.index(min(mm))]  # M1 siempre mayor

        return mn1, mn2, m2


    def filas_columnas2(number):
        m1 = []
        m2 = []
        for divisor in range(1, number+1):
            if (number % divisor) == 0:
                if (divisor <= h and int(number / divisor) <= l) or (divisor <= l and int(number / divisor) <= h):
                    m1.append(divisor)
                    m2.append(int(number / divisor))
        mm = []
        for i in range(len(m1)):
            mm.append(abs(m1[i]-m2[i]))

        #print("Está en la posición: ", mm.index(min(mm)))

        if m1[mm.index(min(mm))] >= m2[mm.index(min(mm))]:    # M1 siempre será el mayor
            mn1 = m1[mm.index(min(mm))]
            mn2 = m2[mm.index(min(mm))]

        else:
            mn1 = m2[mm.index(min(mm))]
            mn2 = m1[mm.index(min(mm))]  # M1 siempre mayor

        #print("Se eligió: ",m1[mm.index(min(mm))],"x", m2[mm.index(min(mm))])
        return mn1, mn2

    # Escogiendo las posiciones de los arboles_____________________________________


    def e_impar(num, pornum):
        v = []
        cont = 0
        copi_num = num
        if (pornum == 1):
            if (num+1) % 2 == 0:
                v.append(int((num+1)/2)-1)
            else:
                v.append(int(num/2)-1)
        elif (pornum == 2):
            if (num % 3) == 0:
                v.append(int(num/3)-1)
                v.append(num-int(num/3))
            elif (num+1) % 3 == 0:
                v.append(int((num+1)/3)-1)
                v.append(num-int((num+1)/3))
            else:
                ayuda = 0
                while((num+ayuda) % 3) != 0:
                    ayuda += 1
                v.append(int((num+ayuda)/3)-1)
                v.append(num-int((num+ayuda)/3))

        elif ((num-pornum) % (pornum-1)) == 0:
            for i in range(0, num, int((num-pornum)/(pornum-1))+1):
                v.append(i)

        else:
            while ((num-pornum) % (pornum-1)) != 0 and num > 0:
                num = num-2
                cont = cont+1
                if num-pornum <= 0:
                    num = 0
                if num > 0 and ((num-pornum) % (pornum-1)) == 0:
                    for i in range(cont, num+cont, int((num-pornum)/(pornum-1))+1):
                        v.append(i)

        return v


    def e_par(num, pornum):
        v = []
        cont = 0
        copi_num = num

        if (pornum == 1):
            if (num+1) % 2 == 0:
                v.append(int((num+1)/2)-1)
            else:
                v.append(int(num/2)-1)

        elif (pornum == 2):
            if (num % 3) == 0:
                v.append(int(num/3)-1)
                v.append(num-int(num/3))
            elif (num+1) % 3 == 0:
                v.append(int((num+1)/3)-1)
                v.append(num-int((num+1)/3))
            else:
                ayuda = 0
                while((num+ayuda) % 3) != 0:
                    ayuda += 1
                v.append(int((num+ayuda)/3)-1)
                v.append(num-int((num+ayuda)/3))

        elif ((num-pornum) % (pornum-1)) == 0:
            for i in range(0, num, int((num-pornum)/(pornum-1))+1):
                v.append(i)

        else:
            while ((num-pornum) % (pornum-1)) != 0 and num > 0:
                num = num-2
                cont = cont+1
                if num-pornum <= 0:
                    num = 0
                if num > 0 and ((num-pornum) % (pornum-1)) == 0:
                    for i in range(cont, num+cont, int((num-pornum)/(pornum-1))+1):
                        v.append(i)
        return v, num


    def escoger(num, pornum):
        if num % 2 == 0:
            v, n = e_par(num, pornum)
            if n == 0:
                num = num-1
                v = e_impar(num, pornum)

        else:
            v = e_impar(num, pornum)
            if v == []:
                num = num-1
                v, n = e_par(num, pornum)

        if v == []:
            aa = []
            for i in range(0, num+1):
                aa.append(i)

            cont = 0
            agg = 0
            while len(v) != pornum:
                if (len(aa[(agg+1):])+len(v)) > pornum:
                    agg = 2*cont
                    v.append(aa[agg])
                    cont = cont+1

                else:
                    for i in range(agg+1, len(aa)):
                        v.append(i)
        return v


    def posicionessel(arb_esc, num_arb, arb_y):
        u = X_camp
        j = Y_camp
        # _______________________________________________________________________________
        h = int((num_arb/arb_y)-2)         # Número de marcadores por surco
        l = int(arb_y-2)                   # Marcadores por hilera
        #print("El número de árboles por surco es ",h)
        #print("El número de árboles por hilera es ",l)

        # Escogiendo filas y columnas__________________________________________________

        # Pares
        primo = 0
        if arb_esc % 2 == 0:

            mm1, mm2 = filas_columnas2(arb_esc)

        # Impares

        elif es_primo(arb_esc) == True and arb_esc != 3 and arb_esc != 1:
            mm1, mm2 = filas_columnas2(arb_esc-1)
            primo = 1

        else:
            mm1, mm2 = filas_columnas2(arb_esc)
            print(mm1, mm2)

        if u > j:       # Se asina mm1 a u
            dist_markersx = u/(mm1+1)
            dist_markersy = j/(mm2+1)
            numx = mm1
            numy = mm2
        else:                 # Se asina mm1 a j
            dist_markersx = u/(mm2+1)
            dist_markersy = j/(mm1+1)
            numx = mm2
            numy = mm1

        return numx, numy, dist_markersx, dist_markersy, primo


    # Dibujamos los margenes del campo
    plt.figure(figsize=(10, 10))
    ax = plt.axes()

    graficacampo(X_camp, Y_camp)
    # plt.figure(figsize=(10,10))

    # Hacemos la trayectoria en el campo
    lineasv, lineash = trayects(X_camp, Y_camp, xm, ym)

    tam = v/3   # Tamaño de los marcadores

    #plt.title("Recorrido en campo")


    #### SURCOS ####################################################################
    if surcos == 1:
        arbolitox = []
        arbolitoy = []
        for j in range(len(lineas_camp)):
            xv = lineas_camp[j]
            a, b = arboles(num_arb, r, xv, yv, esp_arb, v)
            for k in range(len(a)):
                arbolitox.append(a[k])
                arbolitoy.append(b[k])
        arb_selx = []
        arb_sely = []

        # Escogiendo el % de los datos_________________________________________________

        arb_utiles = ((len(arbolitox)/num_arb)-2)*(num_arb-2)

        # _______________________________________________________________________________

        primo = 0
        if es_primo(arb_esc) == True and arb_esc > 3:
            arb_esc = arb_esc-1
            primo = 1

        # _______________________________________________________________________________
        h = int((len(arbolitox)/num_arb)-2)  # Número de arboles por surco
        l = int(num_arb-2)                   # Arboles por hilera

        # Escogiendo filas y columnas__________________________________________________
        mm1, mm2, mm = filas_columnas(arb_esc)
        # _______________________________________________________________________________

        if arb_esc > 1:
            if mm1 > mm2 and mm2 == 1:
                el = escoger(l, mm2)
                eh = escoger(h, mm1)

            elif l % 2 == 0:
                #print("Es l par")
                if ((l-mm1) % (mm1-1)) == 0 and h >= mm2:
                    #print("Con mm1 l funciona")
                    el = escoger(l, mm1)
                    eh = escoger(h, mm2)
                elif ((l-mm2) % (mm2-1)) == 0 and h >= mm1:
                    #print("Con mm2 l funciona")
                    el = escoger(l, mm2)
                    eh = escoger(h, mm1)
                else:
                    #print("l es par pero ninguno sirve")
                    if l > h:
                        el = escoger(l, mm1)
                        eh = escoger(h, mm2)
                    else:
                        #print("h es mayor l")
                        el = escoger(l, mm2)
                        eh = escoger(h, mm1)

            elif h % 2 == 0:
                #print("Es h par")
                if ((h-mm1) % (mm1-1)) == 0 and l >= mm2:
                    el = escoger(l, mm2)
                    eh = escoger(h, mm1)
                elif ((h-mm2) % (mm2-1)) == 0 and l >= mm1:
                    el = escoger(l, mm1)
                    eh = escoger(h, mm2)
                else:
                    if l > h:
                        el = escoger(l, mm1)
                        eh = escoger(h, mm2)
                    else:
                        el = escoger(l, mm2)
                        eh = escoger(h, mm1)
            else:
                if l > h:
                    el = escoger(l, mm1)
                    eh = escoger(h, mm2)
                else:
                    el = escoger(l, mm2)
                    eh = escoger(h, mm1)

        # ARBOLES______________________________________________________________________

        pos_arb_sel_x = []
        pos_arb_sel_y = []
        if arb_esc > 1:
            for b in eh:
                for g in el:
                    #ax.plot(arbolitox[num_arb*(b+1)],arbolitoy[g+1],'or',markersize = 2*np.pi*r*r)
                    pos_arb_sel_x.append(arbolitox[num_arb*(b+1)])
                    pos_arb_sel_y.append(arbolitoy[g+1])

        if primo == 1 or arb_esc == 1:
            if (h+1) % 2 == 0:
                pos_arb_sel_x.append(arbolitox[num_arb*int((h+1)/2)])
                if (l+1) % 2 == 0:
                    #ax.plot(arbolitox[num_arb*int((h+1)/2)],arbolitoy[int((l+1)/2)],'or',markersize = 2*np.pi*r*r)
                    pos_arb_sel_y.append(arbolitoy[int((l+1)/2)])
                else:
                    #ax.plot(arbolitox[num_arb*int((h+1)/2)],arbolitoy[int((l/2))+1],'or',markersize = 2*np.pi*r*r)
                    pos_arb_sel_y.append(arbolitoy[int((l/2))+1])
            elif (l+1) % 2 == 0:
                pos_arb_sel_y.append(arbolitoy[int((l+1)/2)])
                if (h+1) % 2 == 0:
                    #ax.plot(arbolitox[num_arb*int((h+1)/2)],arbolitoy[int((l+1)/2)],'or',markersize = 2*np.pi*r*r)
                    pos_arb_sel_x.append(arbolitox[num_arb*int((h+1)/2)])
                else:
                    #ax.plot(arbolitox[num_arb*(int((h)/2)+1)],arbolitoy[int((l+1)/2)],'or',markersize = 2*np.pi*r*r)
                    pos_arb_sel_x.append(arbolitox[num_arb*(int((h)/2)+1)])

            else:
                #ax.plot(arbolitox[num_arb*(int((h)/2)+1)],arbolitoy[int((l)/2)+1],'or',markersize = 2*np.pi*r*r)
                #ax.plot(arbolitox[num_arb*(int((h)/2)+1)],arbolitoy[int((l)/2)+1],'or',markersize = 2*np.pi*r*r)
                pos_arb_sel_x.append(arbolitox[num_arb*(int((h)/2)+1)])
                pos_arb_sel_y.append(arbolitoy[int((l)/2)+1])

    # SIN SURCOS "#############################################################"
    else:
        #  ## Escogiendo el # de los datos_________________________________________________
        #print("El número total de arboles: ",num_total_arboles)
        arb_utiles = int(((num_total_arboles/arb_y)-2)*(arb_y-2))
        #print("El número total de arboles: ",arb_utiles)
        # Número de marcadores por surco
        h = int((num_total_arboles/arb_y)-2)
        l = int(arb_y-2)                   # Marcadores por hilera
        mm1, mm2 = filas_columnas2(arb_esc)
        # print(mm1,mm2)
        # _______________________________________________________________________________

        # AREAS Y ÁRBOLES A ESCOER

        numx, numy, dist_markersx, dist_markersy, primoa = posicionessel(
            arb_esc, num_total_arboles, arb_y)

        pos_arb_sel_x = []
        pos_arb_sel_y = []

        for i in range(1, numx+1):
            for k in range(1, numy+1):
                pos_arb_sel_x.append(i*dist_markersx)
                pos_arb_sel_y.append(k*dist_markersy)

        # Arboles

        if primoa == 1:
            #ax.plot((X_camp/2),(Y_camp/2),'or',markersize = 30,alpha=0.5)
            pos_arb_sel_x.append(X_camp/2)
            pos_arb_sel_y.append(Y_camp/2)

        ax.plot(pos_arb_sel_x, pos_arb_sel_y, 'or', markersize=30, alpha=0.1)

    # ______________________________________________________________________________

    # MARCADORES____________________________________________________________________


    def markers(posxm, posym, tam):

        ax.add_patch(patches.Rectangle((posxm, posym), tam, tam,
                    edgecolor='black', facecolor='white', fill=True))
        ax.add_patch(patches.Rectangle((posxm+tam, posym), tam, tam,
                    edgecolor='black', facecolor='black', fill=True))
        ax.add_patch(patches.Rectangle((posxm+tam, posym+tam), tam,
                    tam, edgecolor='black', facecolor='white', fill=True))
        ax.add_patch(patches.Rectangle((posxm, posym+tam), tam, tam,
                    edgecolor='black', facecolor='black', fill=True))


    # Marcadores externos
    markers_e = (lineasv[0], lineasv[-1])

    posmarkerscamp_ex_x = []
    posmarkerscamp_ex_y = []

    for i in (markers_e):
        if surcos == 1 and num_markers != -4:
            markers(i-(xm/2), arbolitoy[0]+(ym/2), tam)
            posmarkerscamp_ex_x.append(i-(xm/2))
            posmarkerscamp_ex_y.append(arbolitoy[0])
            markers(i-(xm/2), arbolitoy[-1]-(3*ym/2), tam)
            posmarkerscamp_ex_x.append(i-(xm/2))
            posmarkerscamp_ex_y.append(arbolitoy[-1]-(3*ym/2))
        else:
            if num_markers != -4:
                markers(i-tam, xm-tam, tam)
                posmarkerscamp_ex_x.append(i)
                posmarkerscamp_ex_y.append(xm)
                markers(i-tam, Y_camp-xm-tam, tam)
                posmarkerscamp_ex_x.append(i)
                posmarkerscamp_ex_y.append(Y_camp-xm)

    # Calculando el número de árboles por medida de marcador

    # POSICIÓN DE LOS MARCADORES

    # GENERAR VECTORES DE POSIBLES POSICIONES DE LOS MARCADORES

    posibles_marcadoresx = []
    posibles_marcadoresy = []
    if surcos == 1 and num_markers != -4:
        u = min(posmarkerscamp_ex_x)
        j = min(posmarkerscamp_ex_y)+2*tam
    else:
        if num_markers != -4:
            u = xm+tam
            j = ym+tam
    num_markers_totales = 0
    mark_y = 0

    if num_markers != -4:
        while(u <= max(posmarkerscamp_ex_x)):
            j = min(posmarkerscamp_ex_y)
            while (j <= max(posmarkerscamp_ex_y)):
                posibles_marcadoresx.append(u)
                posibles_marcadoresy.append(j)
                j += (2*tam)
                num_markers_totales += 1

            if u == min(posmarkerscamp_ex_x):
                mark_y = num_markers_totales
            u += (2*tam)

    # _______________________________________________________________________________
    if surcos == 0:
        h = len(lineasv)-2               # Número de surcos (max markers en x)
        l = int(arb_y-3)         # Número máximo de markers en y
    else:
        h = len(lineas_camp)-3               # Número de surcos (max markers en x)
        l = int(num_arb-2)                   # Número máximo de markers en y
    # _______________________________________________________________________________
    primo = 0
    if es_primo(num_markers) == True and num_markers > 3:
        num_markers = num_markers-1
        primo = 1

    if num_markers >= 1:
        mm1, mm2, mm = filas_columnas(num_markers)
    if num_markers > 1:
        j = Y_camp
        if ((h-mm1) % (mm1-1)) == 0:                      # Sí con el mayor funciona
            eh = escoger(h, mm1)
            dist_markersy = j/(mm2+1)
            el = mm2
        elif ((h-mm2) % (mm2-1)) == 0:                    # Sí con el mayor NO funciona
            eh = escoger(h, mm2)
            dist_markersy = j/(mm1+1)
            el = mm1
        else:                                           # # Sí NO

            for i in mm:
                if i > 1:
                    if ((h-i) % (i-1)) == 0:                      # Sí con el mayor funciona
                        #print("Con mm1 h funciona")
                        eh = escoger(h, i)
                        dist_markersy = j/(int(num_markers/i)+1)
                        el = int(num_markers/i)
                        break
            eh = escoger(h, mm2)
            dist_markersy = j/(mm1+1)
            el = mm1
    # MARKERS______________________________________________________________________

    posmarkerscampx = []
    posmarkerscampy = []

    if num_markers > 1:
        for b in eh:
            for i in range(1, el+1):
                if surcos == 1:
                    posmarkerscampx.append(lineas_camp[(b+1)]+(v/2)+xm)
                else:
                    posmarkerscampx.append(lineasv[(b+1)])
                posmarkerscampy.append((i*dist_markersy))

        for i in (posmarkerscampx):
            for k in (posmarkerscampy):
                markers(i-tam, k-tam, tam)
                pepe = 1

    # $ raficando
    # Markers

    if primo == 1 or num_markers == 1:
        if (h+1) % 2 == 0:
            espacio_en_y = arbolitoy[-1]-(ym*3/2)+tam
            if surcos == 1:
                markers(lineas_camp[(int((h+1)/2))]+(v/2)+xm-tam,
                        ((arbolitoy[0]+(ym/2)+tam)+(espacio_en_y))/2, tam)
                posmarkerscampx.append(lineas_camp[(int((h+1)/2))]+(v/2)+xm)
                posmarkerscampy.append(
                    ((arbolitoy[0]+(ym/2)+tam+(espacio_en_y))/2)+tam)
            else:
                markers(lineasv[(int((h+1)/2))]-tam,
                        ((arbolitoy[0]+(ym/2)+tam)+(espacio_en_y))/2, tam)
                posmarkerscampx.append((X_camp/2)-tam)
                posmarkerscampy.append((Y_camp/2)-tam)

        else:
            espacio_en_y = arbolitoy[-1]-(ym*3/2)+2*tam
            if surcos == 1:
                markers(lineas_camp[(int((h)/2))+1] +
                        (v/2)+xm-tam, (Y_camp/2)-tam, tam)
                posmarkerscampx.append(lineas_camp[(int((h)/2))+1]+(v/2)+xm)
                posmarkerscampy.append(
                    ((arbolitoy[0]+(ym/2)+tam+espacio_en_y)/2)+tam)
            else:
                markers(lineasv[(int((h)/2))+1]-tam, (Y_camp/2)-tam, tam)
                posmarkerscampx.append((X_camp/2)-tam)
                posmarkerscampy.append((Y_camp/2)-tam)

    ax.plot(arbolitox, arbolitoy, 'og', markersize=2 *
            np.pi*r*r, label="Árboles")    # Árboles
    ax.plot(pos_arb_sel_x, pos_arb_sel_y, "or", markersize=2 *
            np.pi*r*r, label="Árboles escogidos")    # Árboles esc


    # Posiciones de los marcadores externos
    posmkx = (lineasv[0], lineasv[0], lineasv[-1], lineasv[-1])
    posmky = (arbolitoy[0]+(ym/2)+tam, arbolitoy[-1]-(ym*3/2) +
            tam, arbolitoy[0]+(ym/2)+tam, arbolitoy[-1]-(ym*3/2)+tam)

    if num_markers != -4:
        for i in posmkx:
            posmarkerscampx.append(i)
        for i in posmky:
            posmarkerscampy.append(i)

        ax.plot(posmarkerscampx, posmarkerscampy, '.k', label="Marcadores")
    # ax.plot(pos_arb_sel_x,pos_arb_sel_y,'s')
    ax.set_aspect('equal', adjustable='box')

    ax.set_facecolor("#ebaf42")

    plt.legend()
    plt.savefig("/home/charry/Documents/programacion/trabajo de grado/web/ProjectWeb/WebApp/static/WebApp/img/cultivo.jpg")
    # plt.show()

    # Posiciones de los marcadores (X y Y)

    # posmarkerscampx   Posiciones de los marcadores en "x"
    # posmarkerscampy   Posiciones de los marcadores en "y"


    # Posiciones de los árboles seleccionados (X y Y)

    # pos_arb_sel_x      Posiciones de los árboles en "x"
    # pos_arb_sel_y      Posiciones de los árboles en "y"

    arboles_escogidos = dict(arboles_escogidos_x=pos_arb_sel_x,
                            arboles_escogidos_y=pos_arb_sel_y)
    marcadores = dict(marcadores_x=posmarkerscampx, marcadores_y=posmarkerscampy)

    return arboles_escogidos, marcadores
