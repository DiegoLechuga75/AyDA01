import insertionSort
import mergeSort
import quickSort
import selectionSort
import random as rn
import copy
from time import time


def crearLista(longitud):
    lista = []
    for i in range(0, longitud):
        lista.append(rn.randint(0, 200))
    return lista


if __name__ == "__main__":
    archivo = open("insercionTiempo.csv", "w")
    archivo.write("N;Tiempo\n")
    lista = crearLista(950000)
    x = 100
    for i in range(100, 1510, 100):
        listaNueva = copy.deepcopy(lista[:x])
        inicioTiempo = time()
        insertionSort.ordenamientoInsercion(listaNueva)
        archivo = open("insercionTiempo.csv", "a")
        transcurrido = time() - inicioTiempo
        archivo.write(str(x) + ";" + format(transcurrido, '.5f') + "\n")
        x = x + 100
    archivo.close()
