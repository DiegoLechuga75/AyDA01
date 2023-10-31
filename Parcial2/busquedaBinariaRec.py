def busquedaBinaria(arr, target, bajo, alto):
    if alto >= bajo:

        mitad = bajo + (alto - bajo) // 2

        if arr[mitad] == target:
            return mitad

        elif arr[mitad] > target:
            return busquedaBinaria(arr, target, bajo, mitad - 1)

        else:
            return busquedaBinaria(arr, target, mitad + 1, alto)

    else:
        return None


if __name__ == "__main__":
    data = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    posicion = busquedaBinaria(data, 6, 0, len(data) - 1)

    print("El elemento esta en la posición: " + str(posicion))
