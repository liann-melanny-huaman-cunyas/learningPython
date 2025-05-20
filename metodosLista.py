cursos = ["PHP", "Java", "Python", "C++", "JavaScript"]
nuevos_cursos = ["Ruby", "Go", "Swift"]
#AGREGAR ELEMENTOS al final de la lista
cursos.append("C#")

#INSERTAR ELEMENTOS | en que lugar de la lista , que agregar
cursos.insert(2, "Ruby")

##UBICAR ELEMENTOS
print("Java" in cursos) #True
print("Java" not in cursos) #False

##Indexar elementos
print(cursos.index("Java")) #1

#UNIR DOS LISTAS
cursos.extend(nuevos_cursos)

#COPY
cursos2 = cursos.copy() #copia superficial
cursos3 = cursos[:] #copia profunda

print(cursos2)
print(cursos3)
print(cursos)

##REVERS la lista
revers_list=cursos2[::-1]
print(revers_list)
cursos.reverse() #invierta el orden de la lista
print(cursos)


#SORT | ordenar la lista
cursos.sort() #ordena la lista
print(cursos)

cursos2.sort(reverse=True) #ordena la lista de forma inversa
print(cursos2)

##Eliminar elementos
cursos.remove("Java") #elimina el primer elemento que encuentra
cursos.pop(0)#elimina el elemento en la posicion

print(cursos)
print(len(cursos))

cursos.clear() #elimina todos los elementos de la lista
print(cursos)


