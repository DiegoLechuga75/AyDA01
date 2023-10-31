def mcd(a, b):
    if a < b:
        a, b = b, a
    residuo = 1
    while residuo != 0:
        residuo = a % b
        if residuo == 0:
            return b
        a, b = b, residuo

if __name__ == "__main__":
    print(mcd(124, 6))