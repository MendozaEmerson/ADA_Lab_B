#Mendoza Hilasaca Emerson Danny
#20190631

#Funcion que toma un arreglo y devuelve otro con los valores en posiciones invertidas
def inve(array):
 arreglo = []
 size = len(array) 
 i = 0
 while i < size:
  arreglo.append(size - i)#agrega valores al arreglo desde el tamaño original del arreglo proporcionado
  i += 1
 print(arreglo)

numbers = [1, 2, 3, 4, 5, 6]
print(inve(numbers))