import csv

def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    with open("files/input/data.csv", "r") as archivo:
        file = csv.reader(archivo, delimiter="\t")
            

        resultado = {}

        for fila in file:
            letra = fila[0]  # Columna 1
            valores = fila[4].split(",")  # Columna 5 (lista de "nombre:valor")
            for valor in valores:
                _, numero = valor.split(":")  # Separar "nombre" y "valor"
                if letra in resultado:
                    resultado[letra] += int(numero)
                else:
                    resultado[letra] = int(numero)
    resultado_ordenado = {clave: resultado[clave] for clave in sorted(resultado.keys())}
    return resultado_ordenado

