def permutaciones(arr):
    
    if len(arr) == 0:
        return []
    
    if len(arr) == 1:
        return [arr]
    
    l = []
    
    for i in range(len(arr)):
        m = arr[i]
        
        listaResultante = arr[:i] + arr[i+1:]
        
        for p in permutaciones(listaResultante):
            l.append([m] + p)
    
    return l

if __name__ == "__main__":
    
    data = list("RRRRRUUU")
    for p in permutaciones(data):
        print(p)