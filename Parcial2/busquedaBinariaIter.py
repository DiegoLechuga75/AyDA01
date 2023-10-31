def busquedaBinaria(arr, target):

    bajo = 0
    alto = len(arr)

    while alto >= bajo:

        mitad = bajo + (alto - bajo) // 2

        if arr[mitad] == target:
            return mitad

        if arr[mitad] > target:
            alto = mitad - 1
        else:
            bajo = mitad + 1

    return None

if __name__ == "__main__":
    data = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    posicion = busquedaBinaria(data, 6)

    print("El elemento esta en la posición: " + str(posicion))
