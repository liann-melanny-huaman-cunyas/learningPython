###Tuplas en Python
# Las tuplas son similares a las listas, pero son inmutables, 
# lo que significa que no se pueden modificar una vez creadas.
"""
Estructua de datos que permite almacenar una coleccion de elementos
"""
#indices      0         1        2        3        4
#negativos   -5       -4       -3       -2       -1
setings = ("localhost", 8080, "admin", "password",True)
print(setings)
print(type(setings))

print(setings[0])

##segunda forma de crear una tupla
setings2 = tuple(["localhost", 8080, "admin", "password",True])
print(setings2)
print(type(setings2))
print(setings2[2])

##tercera forma de crear una tupla
setings3 = "localhost", 8080, "admin", "password",True
print(setings3)
print(type(setings3))
print(setings3[3])

"""
Desampequetado de Tuplas
"""

mascotas = ("afrodita", "cassie","kanon","butckus")

# Asignar cada elemento de la tupla a una variable

## primera forma de desempaquetar
var1 = mascotas[0]
var2 = mascotas[1]
var3 = mascotas[2]
var4 = mascotas[3]

print(var1 ,var2, var3, var4)

## segunda forma de desempaquetar
var1, var2, var3, var4 = "afrodita", "cassie","kanon","butckus"
print(var1 ,var2, var3, var4)
print(type(var1))

## tercera forma de desempaquetar
var1, var2, var3, var4 = mascotas
print(var1 ,var2, var3, var4)
print(type(var1))

## cuarta forma de desempaquetar
var1,*var2,var3 = mascotas
print(var1 ,var2, var3)
print(type(var2))

## quinta forma de desempaquetar
var1,*var2,var3,var4 = mascotas
print(var1 ,var2, var3,var4)
print(type(var2))

## sexta forma de desempaquetar
var1,*var2,var3,var4,var5 = mascotas
print(var1 ,var2, var3,var4,var5)
print(type(var5))

## septima forma de desempaquetar
# El guion bajo (_) se usa convencionalmente para ignorar valores que no nos interesan
var1, _, var3, var4 = mascotas
print(var1, var3, var4)

"""
Zip
Unir dos o mas listas en una sola lista de tuplas
"""
##Asigna a cada elemento de la lista una tupla
## con el mismo indice de la otra lista

users = ["admin", "user", "guest"]
emails = ["admin@localhost", "user@localhost", "guest@localhost"]
passwords = ["admin", "user", "guest"]

reponse =list (zip(users, emails))
print(reponse)

register = list(zip(users, emails, passwords))
print(register)

"""
    Funciones de tuplas
    - count: cuenta el numero de veces que un elemento aparece en la tupla
    - index: devuelve el indice del primer elemento que coincide con el valor especificado
    - len: devuelve el numero de elementos de la tupla
    - max: devuelve el elemento mayor de la tupla
    - min: devuelve el elemento menor de la tupla
    - sum: devuelve la suma de los elementos de la tupla
    - sorted: devuelve una lista ordenada de los elementos de la tupla
    - all: devuelve True si todos los elementos de la tupla son verdaderos
    - any: devuelve True si al menos un elemento de la tupla es verdadero
    - tuple: convierte una lista en una tupla
    - str: convierte una tupla en una cadena
    - list: convierte una tupla en una lista
    - dict: convierte una tupla en un diccionario
    - set: convierte una tupla en un conjunto
    - frozenset: convierte una tupla en un conjunto inmutable
    - bytes: convierte una tupla en un objeto de bytes
    - bytearray: convierte una tupla en un objeto de bytes mutable
    - memoryview: convierte una tupla en un objeto de vista de memoria
    - fromkeys: crea un diccionario a partir de una tupla
    - get: devuelve el valor de una clave en un diccionario
    - items: devuelve una lista de tuplas con los elementos de un diccionario
    - keys: devuelve una lista de claves de un diccionario
    - pop: elimina un elemento de un diccionario
    - popitem: elimina el ultimo elemento de un diccionario
    - setdefault: devuelve el valor de una clave en un diccionario, si no existe, la crea
"""

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(numeros.count(1)) # cuenta el numero de veces que un elemento aparece en la tupla
print(numeros.index(1)) # devuelve el indice del primer elemento que coincide con el valor especificado
print(len(numeros)) # devuelve el numero de elementos de la tupla
print(max(numeros)) # devuelve el elemento mayor de la tupla
print(min(numeros)) # devuelve el elemento menor de la tupla
print(sum(numeros)) # devuelve la suma de los elementos de la tupla
print(sorted(numeros)) # devuelve una lista ordenada de los elementos de la tupla

print(sorted(numeros, reverse=True)) # devuelve una lista ordenada de los elementos de la tupla