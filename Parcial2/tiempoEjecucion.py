import insertionSort
import mergeSort
import quickSort
import selectionSort
import bubbleSort
import random as rn
import copy
from time import time


def crearLista(longitud):
    lista = []
    for i in range(0, longitud):
        lista.append(rn.randint(0, 200))
    return lista


if __name__ == "__main__":
    archivo = open("m4.csv", "w")
    archivo.write("N;Tiempo\n")
    lista = crearLista(950000)
    x = 100
    for i in range(100, 15100, 100):
        listaNueva = copy.deepcopy(lista[:x])
        inicioTiempo = time()
        size = len(listaNueva)
        quickSort.quickSort(listaNueva, 0, size - 1)
        archivo = open("m4.csv", "a")
        transcurrido = time() - inicioTiempo
        archivo.write(str(x) + ";" + format(transcurrido, '.5f') + "\n")
        x = x + 100
    archivo.close()
