def maxSuma(n,s):
    max=0
    suma=0
    for i in range(n):
        if suma+s[i] > 0:
            suma=suma+s[i]
        else:
            suma=0
        if suma>max:
            max=suma
    return max;

if __name__ == "__main__":
    
    s=[1,2,3,4,5,6,7,8,9,10]
    
    print(maxSuma(6, s))