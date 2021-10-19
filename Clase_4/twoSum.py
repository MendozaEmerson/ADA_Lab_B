#Mendoza Hilasaca Emerson Danny
#Funcion que verifica la suma de valores de indices distintos.


def twoSum(array):
    for i, e in enumerate(array):
        for j, a in enumerate(array):
            if e != a and i + j == 10:  # indices diferentes suma igual a 10
                return True
    return False


array = [3, 0, 5, 1, 0, 4, 8]

print(twoSum(array))

#La complejidad es de O(n^2)
