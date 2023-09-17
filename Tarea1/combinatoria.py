import numpy as np

def combinaciones(elementos, r):
    tuplaDeElementos = tuple(elementos)
    n = len(tuplaDeElementos)
    if r > n:
        return
    indices = np.arange(r)
    yield tuple(tuplaDeElementos[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n -r:
                break
        else:
                return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(tuplaDeElementos[i] for i in indices)

if __name__ == "__main__":
    
    print([x for x in combinaciones("ABCD", 2)])