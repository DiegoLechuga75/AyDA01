from itertools import permutations

def listPermutations(arr):
    perm = list(permutations(arr))
    return perm

if __name__ == "__main__":
    
    elements = ["R1", "R2", "R3", "R4", "R5", "U1", "U2", "U3"]
    print(listPermutations(elements))
    
