def dosMax (numeros):
    max1=numeros[0]
    for i in numeros:
        if(i>max1):
            max1=i
    numeros.remove(max1)
    max2=numeros[0]
    for i in numeros:
        if(i>max2):
            max2=i
    return max1,max2;    

if __name__ == "__main__":

    numeros=[2000,400,1000,50]
    print(dosMax(numeros))