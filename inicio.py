"""
Variables en Python
"""

# En Python no es necesario declarar el tipo de variable
# Se asigna el valor a la variable y Python infiere el tipo de variable
## <snake_case> = <valor>

##Tipos de variables | En Python todo es objeto

#int
gato = 5
print(gato)
print(type(gato))

#float
gato = 5.5
print(gato)
print(type(gato))

#str
gato = "afrodita"
print(gato)
print(type(gato))

#bool
gato = True
print(gato)
print(type(gato))

#bytes
gato = b"hola"
print(gato)
print(type(gato))

#list
gato = [1, 2, 3, 4, 5]
print(gato)
print(type(gato))

#tuple
gato = (1, 2, 3, 4, 5)
print(gato)
print(type(gato))

#dict
gato = {"nombre": "afrodita", "edad": 5}
print(gato)
print(type(gato))

#set
gato = {1, 2, 3, 4, 5}
print(gato)
print(type(gato))

#frozenset
gato = frozenset({1, 2, 3, 4, 5})
print(gato)
print(type(gato))

#bytearray
gato = bytearray(b"hola")
print(gato)
print(type(gato))

#memoryview
gato = memoryview(b"hola")
print(gato)
print(type(gato))

#None
gato = None
print(gato)
print(type(gato))

#complex
gato = 5 + 5j
print(gato)
print(type(gato))

#range
gato = range(5)
print(gato)
print(type(gato))
