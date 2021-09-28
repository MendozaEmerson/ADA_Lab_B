
#Mendoza Hilasaca Emerson Danny
#20190631
#Ejercicio 3
from timeit import default_timer

def ntime(array, answer):
    length = len(array)
    for x in range(length):
        if array[x] == answer:
            return True
    return False

array = (range(300))
inicio = default_timer()
ntime(array, 231)
fin = default_timer()

tiempo = fin - inicio
print(tiempo )