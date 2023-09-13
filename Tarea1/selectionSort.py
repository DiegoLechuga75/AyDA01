def ordenamientoSeleccion(arr, size):
    for i in range(size):
        minI = i
        
        for j in range(i + 1, size):
            if arr[j] < arr[minI]:
                minI = j
                
        (arr[i], arr[minI]) = (arr[minI], arr[i])
        
if __name__ == "__main__":
    
    data = [-2, 45, 0, 11, -9]
    size = len(data)
    ordenamientoSeleccion(data, size)
    print(data)