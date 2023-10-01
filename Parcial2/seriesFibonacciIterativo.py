def fib(n):
    if n <= 1:
        return n
    x = 0
    fibMayor = 1
    fibMenor = 0
    for i in range(n):
        print(fibMenor)
        x = fibMenor + fibMayor
        fibMenor = fibMayor
        fibMayor = x
    return fibMenor

if __name__ == "__main__":
    print(fib(10))