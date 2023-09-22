import numpy as np 

def calcularPi (n):
    i=2
    serie=1
    while(i<n):
        serie+=1/(i*i)
        i+=1
    resultado = np.sqrt(6*serie)
    return resultado

if __name__ == "__main__":

    print(calcularPi(10000000))