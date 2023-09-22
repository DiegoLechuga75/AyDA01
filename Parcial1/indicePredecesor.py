def predecesorLength (arr):
    for i in range(0, len(arr)):
        if len(arr[i])<len(arr[i+1]):
            return i
        
if __name__ == "__main__":

    arr = ['Tomas', 'Bruno', 'Dan', 'Elie', 'Zeke']
    
    print(predecesorLength(arr))
