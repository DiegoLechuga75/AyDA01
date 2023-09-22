def calcularRaizCuadrada(x):

    raiz = x
    precision = 10 ** (-10)
    
    while abs(x - raiz * raiz) > precision:
        raiz = (raiz + x / raiz) / 2
        
    return raiz

if __name__ == "__main__":

    print(calcularRaizCuadrada(25))