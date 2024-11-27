"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    lfinal = []
    archivo = open("files\input\data.csv") 
    file = csv.reader(archivo, delimiter= "\t")
    lbase = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj"]
    lcod =[]
    for f in file:
        #archivo.seek(0)
        sep = f[4].split(",")
        for a in sep:
            lcod.append(a)
        #nlista = f[3].split(",")
        #print(nlista)

    lotra = []
    for a in lbase:
        lotra = []
        for z in lcod:
            if a in z:
                casilla = z.split(":")
                #print(casilla)
                lotra.append(int(casilla[1]))
        final = (a,  int(min(lotra)), int(max(lotra)))
        lfinal.append(final)
    return(lfinal)