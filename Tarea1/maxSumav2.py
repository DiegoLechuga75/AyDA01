import numpy as np

def maxSuma(s, n):
    suma = np.zeros((n, n))
    max_sum = 0
    for i in range(n):
        for j in range(i, n):
            suma[i][j] = suma[i][j - 1] + s[j]
            if suma[i][j] > max_sum:
                max_sum = suma[i][j]
        suma[i][i] = s[i]
        if suma[i][i] > max_sum:
            max_sum = suma[i][i]
    return max_sum

if __name__ == "__main__":
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(maxSuma(s, 6))
