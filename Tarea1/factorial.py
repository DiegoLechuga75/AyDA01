def obtenerFactorial (n):
    if n == 1 or n == 0:
        return 1
    return n * obtenerFactorial(n-1)

print(obtenerFactorial(10))