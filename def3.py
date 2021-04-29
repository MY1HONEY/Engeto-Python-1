# transform dictionary to tuple by def
dict = {1 : "one", 2 : "two"}

def transform(dict):
    a = list(dict.items())
    return print(a)

transform(dict)

# merge dictionaries to the new one
A = {1 : "one", 2 : "two"}
B = {3 : "three", 4 : "four"}

def merge(A, B):
    C = {**A, **B}
    for key, value in C.items():
        if key in A and key in B:
            dict[key] = [value, A[key]]
    return C

C = merge(A, B)
print(C)

# merge dictionaries to the new one and keep values in same keys
A = {1 : "one", 2 : "two"}
B = {2 : "dva", 3 : "three"}

def merge(A,B):
    merged = A.copy()
    merged.update(B)
    
    for key in A.keys():
        if key in B.keys():
           merged[key] = [A[key],B[key]]
    return merged

print(merge(A,B))