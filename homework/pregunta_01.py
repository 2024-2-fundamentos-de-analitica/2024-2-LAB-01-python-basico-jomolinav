"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    
    Rta/
    214

    """
    a = 0
    archivo = open("files/input/data.csv") 
    file = csv.reader(archivo, delimiter= ",")
    for f in file:
        print(f)
        a =  a + int(((f[0])[2]))

    return a
