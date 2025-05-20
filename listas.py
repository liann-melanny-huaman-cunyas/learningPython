## Una listaes una estrutura de datos que permite almacenar una coleccion de elementos
# # de diferentes tipos, como enteros, cadenas, booleanos, etc.

"""
<variables> = [<elemento1>, <elemento2>, <elemento3>, ...]
"""
#            0         1        2        3        4
#           -5        -4       -3       -2       -1
list_cats = ["afrodita", "miau", "gato", "felino", "peludo"] #string(5)

print(list_cats)
print(type(list_cats))
print(list_cats[0])
value = list_cats[2]
print(value)
value = list_cats[-3]
print(value)

##  Nueva lista a partir de una lista existente
list_cats2 = list_cats[0:3]
print(list_cats2)

##  Nueva lista a partir de una lista existente
list_cats3 = list_cats[0:4:3]
print(list_cats3)
##  Nueva lista a partir de una lista existente
list_cats4 = list_cats[::3]#con saltos de 2 a 2
print(list_cats4)
##  Nueva lista a partir de una lista existente
list_cats5= list_cats[2::]
print(list_cats5)
##shaloww copy
list_cats6 = list_cats.copy()
print(list_cats6)
##deep copy
list_cats7 = list_cats[:]
print(list_cats7)
