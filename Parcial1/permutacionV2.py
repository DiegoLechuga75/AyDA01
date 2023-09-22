from itertools import permutations

def listPermutations(arr):
    perm = list(permutations(arr))
    return perm

if __name__ == "__main__":
    
    elements = ["R", "R", "R", "R", "R", "U", "U", "U"]
    uniqueElements = set(listPermutations(elements))
    print(uniqueElements)
    
