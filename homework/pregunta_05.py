"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    archivo = open("files\input\data.csv") 

    lista =["A", "B", "C", "D", "E"]
    lac = []
    lfinal = []
    for a in lista:
        archivo.seek(0)
        lac = []
        file = csv.reader(archivo, delimiter= "\t")
        for z in file:
            if a == z[0]:
                lac.append(z[1])
        final = (a, int(max(lac)), int(min(lac)))
        lfinal.append(final)
    return(lfinal)