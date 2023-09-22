def factorial (n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def permuta(n, r):
    return (factorial(n)/factorial(n-r))

if __name__ == "__main__":
    
    print(permuta(5, 5))