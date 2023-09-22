def particion(arr, bajo, alto):
    
    pivote = arr[alto]
    i = bajo - 1
    
    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
            
    (arr[i + 1], arr[alto]) = (arr[alto], arr[i + 1])
    
    return i + 1

def quickSort(arr, bajo, alto):
    if bajo < alto:
        
        pi = particion(arr, bajo, alto)
        
        quickSort(arr, bajo, pi - 1)
        
        quickSort(arr, pi + 1, alto)
        
if __name__ == "__main__":
    
    data = [8, 7, 2, 1, 0, 9, 6]
    print("Arreglo sin ordenar")
    print(data)
    
    size = len(data)
    
    quickSort(data, 0, size - 1)
    
    print('Arreglo ordenado de forma ascendente:')
    print(data)
