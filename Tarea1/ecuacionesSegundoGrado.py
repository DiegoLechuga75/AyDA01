import numpy as np

def x1 (a, b, c):
    determinante = (b*b)-(4*(a*c))
    raiz = np.sqrt(determinante)
    numerador = -b - raiz
    resultado = numerador/(2*a)
    return resultado

def x2 (a, b, c):
    determinante = (b*b)-(4*(a*c))
    raiz = np.sqrt(determinante)
    numerador = -b + raiz
    resultado = numerador/(2*a)
    return resultado

def ecuacionSegundoGrado (a, b, c):
    i=0
    while(i<2):
        if(i==1):
            print(x1(a, b, c))
        else:
            print(x2(a, b , c))
        i+=1
        
ecuacionSegundoGrado(1, -4, 3)