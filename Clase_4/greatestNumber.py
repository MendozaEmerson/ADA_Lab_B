#Mendoza Hilasaca Emerson Danny
#Funcion que devuelve el valor mas grande de un arreglo.


def greatestNumber(array):
    menor = 0
    for x in array:
        if x > menor:
            menor = x
    return menor


array = [1, 89, 34, 123]
print(greatestNumber(array))
#Complejidad de O(n)
