def ordenamientoInsercion(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            
        arr[j + 1] = key
        
if __name__ == "__main__":
    
    data = [9, 5, 1, 4, 3]
    ordenamientoInsercion(data)
    print(data)