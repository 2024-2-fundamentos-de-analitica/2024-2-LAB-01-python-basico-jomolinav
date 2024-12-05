"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    lbase = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
    lfinal = []
    archivo = open("files\input\data.csv") 
    for z in lbase:
        archivo.seek(0)
        letras = []
        file = csv.reader(archivo, delimiter= "\t")

        for a in file:
            if int(a[1]) == z:
                if a[0] not in letras:
                    letras.append(a[0])

        final = (z, sorted(letras))
        lfinal.append(final)

    return(lfinal)
