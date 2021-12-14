# TieRopes.py

def ropes(k, A):
    # Funcion que toma un entero y un arreglo para devolver 
    # el número de cuerdas cuya longitud sea mayor o igual que K sea máximo.
    res = 0
    max = 0
    i = 0
    for count in A: 
        
        i = i + A[i]
        res += 1

        if i >= k:
            if res > max:
                max = res
            i = 0

        if A[i] == k:
            res = 0 
            i = 0   

    return max

arreglo = [1, 2, 3, 4, 1, 1, 3]

print(ropes(4, arreglo))
