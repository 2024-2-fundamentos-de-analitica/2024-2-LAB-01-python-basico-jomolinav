"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv 

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    archivo = open("files/input/data.csv") 
    file = csv.reader(archivo, delimiter= ",")
    a = []
    l = []
    lfinal = []

    for f in file:
        a.append((f[0])[0])
    for z in a:
        if z not in l:
            l.append(z)
    for h in l:
        conteo = (h, a.count(h))

        lfinal.append(conteo)

    lfinal.sort(key= lambda x:x[0])
    return(lfinal)