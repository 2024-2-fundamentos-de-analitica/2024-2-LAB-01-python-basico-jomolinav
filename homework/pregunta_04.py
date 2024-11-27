"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    archivo = open("files\input\data.csv") 
    file = csv.reader(archivo, delimiter= "\t")

    acumulados = {}

    for fila in file:
        calend = fila[2]
        calend = calend[5:7]
        if calend in acumulados:
            acumulados[calend] += 1
        else:   
            acumulados[calend] = 1
        resultado = sorted(acumulados.items())
    return(resultado)
