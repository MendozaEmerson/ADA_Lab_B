def search(array, entero):
    for x in array:
        if x == entero:
            return True
    return False


arreglo = [1, 3, 24, 56, 234, 78]
print(search(arreglo, 234))
