#Mendoza Hilasaca Emerson Danny
#20190631

#Funcion que toma un arreglo y devuelve dos arreglos un con valores pares y otro con impares del arreglo tomado
def div(array):
 par = []
 impar = []
 i = 0
 for x in array:
  if x % 2 == 0:#condional que verifica un numero par
   par.append(x)
  else:
   impar.append(x)
  i += 1
 print(par, impar)
 
numbers = [1, 2, 3, 4, 5, 6]
print(div(numbers))