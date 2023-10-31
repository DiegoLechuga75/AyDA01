def sumaCadenas(string):
    listaNumero = list(string)
    suma = 0
    if len(listaNumero) == 1:
        return int(listaNumero[0])
    for i in listaNumero:
        suma += int(i)
    return suma

if __name__ == "__main__":
    print(sumaCadenas("456"))