def mcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return mcd(b, a % b)

if __name__ == "__main__":
    print(mcd(8, 12))