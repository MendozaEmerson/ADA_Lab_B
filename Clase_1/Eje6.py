#Mendoza Hilasaca Emerson Danny
#20190631
#Funcion que toma un valor numerico y un string para imprimir el string en un marco con espacios igual al valor numerico
def marco(word, entero):
 c1 = ((len(word)* entero) + 4) * '*' + "\n"
 space = "*" + ((len(word)* entero) + 2) * " " + "*\n"
 palabra ="*" + " " * 5 + word + " " * 5+ "*" + "\n"

 print(c1 + (space * entero) + palabra + (space * entero) + c1) 

print(marco("Hola", 3))