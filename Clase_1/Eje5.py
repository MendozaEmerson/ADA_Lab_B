#Mendoza Hilasaca Emerson Danny
#20190631
#Funcion que toma una palabra e imprime la misma en un marco
def text(word):
  cab = (len(word) + 4) * '*' + "\n"#cabezeras del marco
  space = "*" + (len(word) + 2) * " " + "*\n"#espacios
  pal = "*" + word + "*\n"#espacios y palabra
  
  print(cab + space + pal + space + cab)

word = "Hello World!"
text(word)
