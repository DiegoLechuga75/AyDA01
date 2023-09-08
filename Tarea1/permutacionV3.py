def factorial (n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def permutaciones(n):
    numeros=[]
    for i in range(n):
        numeros.append(i+1)
    print(numeros)
    print()
    for i in range(1, factorial(len(numeros))):
        m = n-2
        while (numeros[m]>numeros[m+1]):
            m-=1
        k=n
        while (numeros[m]>numeros[k-1]):
            k-=1
        
        
if __name__ == "__main__":
    
    permutaciones(5)