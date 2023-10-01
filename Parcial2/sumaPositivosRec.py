def sumaPositivos(n):
    if n <= 1:
        return n
    return n + sumaPositivos(n - 1)

if __name__ == "__main__":
    print(sumaPositivos(55))