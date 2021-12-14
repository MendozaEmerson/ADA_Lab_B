# Maxnonoverlapping.py

def MaxSegments(A,B):
    # Dado dos arreglos la funcion retorna
    # la cantidad maxima de segmentos no sobrepuestos. 
    i = 0
    valor = 0
    while i < len(A):
        if(A[i] > B[i]):
            return 0
        if(B[i - 1] > B[i]):
            return 0
        i += 1

    m = 0
    while m < len(A):
        for cout in A:
            n = 0
            if cout > B[n]:
                valor += 1
                n += 1
        m += 1  

    return valor

A = [1, 3, 4, 6]
B = [2, 5, 6, 7]

print(MaxSegments(A,B))


