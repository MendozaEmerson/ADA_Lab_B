#Ejercicio 2

def matched(w, m):
    w[0] = m
    return w

def verif(w):
    if w[0] != " ":
        return True
    return False

def preferen(w, m):
    if searchWord(w, w[0]) > searchWord(w, m):
        return True
    return False

def searchWord(array, word):
    count = 1
    for x in array:
        if x == word:
            break
        count += 1
    return count

def pair(w, m):
    if verif(w) == False:
        matched(w, m)
    else:
        if preferen(w, m) == True:
            matched(w, m)
    return w

arreglo = [" ", "Rogelio", "Romeo", "Santi", "Braulio", "Aurelio"]

arreglo2 = ["Rogelio", "Aurelio", "Braulio", "Santi", "Romeo", "Rogelio"]

print(pair(arreglo, "Santi"))
print(pair(arreglo2, "Braulio"))