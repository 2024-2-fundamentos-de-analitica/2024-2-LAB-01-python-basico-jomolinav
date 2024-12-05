"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    archivo = open("files/input/data.csv")  
    file = csv.reader(archivo, delimiter= "\t")

    lbase = ["a", "b", "c", "d", "e", "f", "g"]
    dicfin = {}
    for letra in lbase:
        archivo.seek(0)
        file = csv.reader(archivo, delimiter= "\t")
        cont = 0 
        for fila in file:
            if letra in fila[3]:
                cont = cont + int(fila[1])
        dicfin[letra] = cont 
    return(dicfin)
