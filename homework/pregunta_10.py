"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    archivo = open("files/input/data.csv")  
    file = csv.reader(archivo, delimiter= "\t")
    lfin = []
    for a in file:

        aux1 = a[3].split(",")
        aux2  = a[4].split(",")
        z = (a[0], len(aux1), len(aux2))
        lfin.append(z)
    return(lfin)