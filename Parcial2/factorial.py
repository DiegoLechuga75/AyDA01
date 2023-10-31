def obtenerFactorial (n):
    if n == 1 or n == 0:
        return 1
    return n * obtenerFactorial(n-1)

if __name__ == "__main__":

    print(obtenerFactorial(10))
