"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    dbase = {"aaa" : 0, "bbb":0, "ccc":0, "ddd":0, "eee":0, "fff":0, "ggg":0, "hhh":0, "iii":0, "jjj":0} 

    archivo = open("files/input/data.csv")  
    file = csv.reader(archivo, delimiter= "\t") 
    lbvalores = []
    for z in file: 
        valores = z[4].split(",")
        for a in valores:
            lbvalores.append(a)
    lfinal  = []
    for z in lbvalores:
        lfinal.append(z[0:3])



    for clave in dbase:
        contador = lfinal.count(clave)
        dbase[clave] = contador
    return(dbase)