def calcularRaizCuadrada(x):

    raiz = x
    presicion = 10 ** (-10)
    
    while abs(x - raiz * raiz) > presicion:
        raiz = (raiz + x / raiz) / 2
        
    return raiz

print(calcularRaizCuadrada(25))