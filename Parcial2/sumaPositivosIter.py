def sumaPositivos(n):
    if n <= 1:
        return n
    suma = 0
    for i in range(n+1):
        suma += i
    return suma

if __name__ == "__main__":
    print(sumaPositivos(55))