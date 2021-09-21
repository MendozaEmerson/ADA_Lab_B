#Mendoza Hilasaca Emerson Danny
#20190631
#Funcion que toma tres valores numericos y devuelve un arreglo con los valores ordenados de manera ascedente
def order(x, y, z):
 asc = [0, 0, 0]
 if min(x,y) != min(y, z):#verificacion de que y no sea minima
  asc[1] = y
  if min(x,y) < min(y, z):
   asc[0] = x
   asc[2] = z
  else:
   asc[0] = z
   asc[2] = x
 else:# "y" como el valor mas minimo
  asc[0] = y
  if min(x,z) == x:
   asc[1] = x
   asc[2] = z
  else:
   asc[1] = z
   asc[2] = x
 print(asc)

#funcion que toma dos valores numericos y devuelve em minimo de ellos
def min(x, y):
 min = x 
 if min > y:
  return y

 return min

print(order(3, 1, 4))