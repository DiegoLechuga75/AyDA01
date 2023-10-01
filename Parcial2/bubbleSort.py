def ordenamientoBurbuja(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux

if __name__ == "__main__":
    data = [5, 434, 44, 9, 11, 0, -3]

    ordenamientoBurbuja(data)

    print("Arreglo ordenado")
    print(data)