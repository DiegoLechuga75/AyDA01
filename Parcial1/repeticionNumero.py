import numpy as np

def repeticion(n, arr):
    contador=0
    for num in arr:
        if n == num:
            contador+=1
    return contador

if __name__ == "__main__":
    
    arr=np.random.randint(0, 500, 500, int)
    print(arr)
    print()
    print(repeticion(250, arr))