title = "Curso de Ciencia de Datos"

## Volver todos minusculas
print (title.lower())
## Volver todos mayusculas
print (title.upper())
##Capitalizar la primera letra de cada palabra
print (title.capitalize()) ## 	Mayúscula solo al inicio de la cadena
print (title.title()) #capitaliza la primera letra de cada palabra
##contar el numero de veces que aparece una letra
print (title.count("C"))


##STARTWITH
print (title.startswith("Curso")) #True
##ENDWITH
print (title.endswith("Datos")) #True

##quiero buscar una palabra sin importar mayusculas o minusculas
print (title.lower().count("ciencia"))


frase = "    Hay mucho que aprender en este curso   "
print (frase)
##strip
print (frase.strip()) #elimina los espacios en blanco al inicio y al final de la cadena
##lstrip
print (frase.lstrip()) #elimina los espacios en blanco al inicio de la cadena
##rstrip
print (frase.rstrip()) #elimina los espacios en blanco al final de la cadena


frase2= "Progracamacion en Python"

##metodo find es case sensitive
##¿que es find?
##find devuelve el indice de la primera ocurrencia de la subcadena
##si no encuentra la subcadena devuelve -1
##si encuentra la subcadena devuelve el indice de la primera ocurrencia
print (frase2.find("n")) #0
print (frase2.find("p")) #-1


##isnumeric
## ¿que es isnumeric?
##isnumeric devuelve True si la cadena es un numero
##si la cadena no es un numero devuelve False


##isalpha
## ¿que es isalpha?
##isalpha devuelve True si la cadena es una letra
##si la cadena no es una letra devuelve False


print ("123".isnumeric()) #True
print ("123.45".isnumeric()) #False
print ("123a".isnumeric()) #False
print ("123a".isalpha()) #False