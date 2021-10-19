#Mendoza Hilasaca Emerson Danny
#Funcion que suma el valor del indice par mas otros valores del mismo arreglo.


def every_other(array):
    for x in array:
        i = 0
        if i % 2 == 0:  #verifica indice par
            for y in array:
                print(x + y)
            print(" ")
        i += 1


arreglo = [10, 2, 4]

every_other(arreglo)
# Complejidad de O(n^2)