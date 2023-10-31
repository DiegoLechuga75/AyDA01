def sumaCadenas(numeroTexto):
    listaNumero = list(numeroTexto)
    if len(listaNumero) == 1:
        return int(listaNumero[0])
    elementoSuma = listaNumero[0]
    listaNumero.pop(0)
    cadenaResultante = "".join(listaNumero)
    suma = int(elementoSuma) + int(sumaCadenas(cadenaResultante))
    return suma

if __name__ == "__main__":
    print(sumaCadenas("456"))