# numbers = [ 1,2,3,4,5,6,7,8]

# #sumar el primer y el ultimo elemento
# print(numbers[0] + numbers[7])

# #simar todos los elementos
# print(numbers[1] + numbers[2]+ numbers[3] + numbers[4] + numbers[5] + numbers[6]+ numbers[7])

# ##una lista de longitud 10 de tipo string
# strings_list=["ana","maria","jose","luis","pablo","carlos","javier","jorge","pedro","juan"]

# #imprimir una nueva lista que tennga los 3 primeros y 3 ultimos elementos
# new_list = strings_list[0:3] + strings_list[-3:]
# ##otra forma de hacerlo
# new_list = strings_list[:3] + strings_list[-3:]
# print(new_list)

# ##imprimir si codigo facilito esta en el list
# print("CodigoFacilito" in strings_list)

# ##imprimir una matriz 3x3  e imprimir si el primer elemento de cada fila es un numero par
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     if row[0] % 2 == 0:
#         print(f"El primer elemento de la fila {row} es par")
#     else:
#         print(f"El primer elemento de la fila {row} es impar")

# ##que es row
# ##row es una variable que representa cada fila de la matriz
# ##en cada iteracion del bucle for, row toma el valor de una fila de la matriz

# ##otra forma de hacerlo
# for i in range(len(matrix)):
#     if matrix[i][0] % 2 == 0:
#         print(f"El primer elemento de la fila {i} {matrix[i][0]} es par")
#     else:
#         print(f"El primer elemento de la fila {i} {matrix[i][0]} es impar")

# ##definir una tupla d elongitud 3 

# my_tupla = "liann","24","mujer"
# print(my_tupla)

# my_tuple = ("liann", 24, "mujer","ingeniera","sistemas")
# var1, _, _, var4, var5 = my_tuple

# print(var1, var4, var5)

# my_list=[1,2,3,4,5,6,7,8]
# new_list=tuple(my_list)

# even_tuple = tuple(filter(lambda x: x % 2 == 0, my_list))
# print(even_tuple)

# par_tuple =tuple(x for x in my_list if x % 2 == 0)
# print(par_tuple)

# par_list = []
# for i in my_list:
#     if i % 2 == 0:
#         print(i)
#         par_list.append(i)

# par_tuple2 = tuple(par_list)
# print("Tupla de pares:", par_tuple2)

# #---------------------------------------------------------------------
# ## realizar in detector de palindromos

# palabra1= input("Ingrese una palabra: ")

# ##priimero todo a minuscula
# detector =palabra1.lower().strip()

# ##invertir la palabra

# detector2 = detector[::-1]

# ## ¿que hace el slice?
# ## el slice [::-1] invierte la cadena
# ## el slice [::-1] significa que se va a recorrer la cadena desde el final hasta el principio

# ##otra forma de invertir
# detector3 = ""
# for i in range(len(detector)-1, -1, -1):
#     detector3 += detector[i]
#     ## ¿que hace el range?
#     ## el range(len(detector)-1, -1, -1) recorre la cadena desde el final hasta el principio


# if  detector == detector2:
#     print("True")
# else:
#     print("False")

# #---------------------------------------------------------------------
# name = 'CodigoFacilito'
# print(name.capitalize()) # Capitaliza la primera letra de la cadena
# #---------------------------------------------------------------------

# #imprimir si la ultima letra de la cadena es una vocal

# palabra_vocal = input("Ingrese una palabra: ")

# print(palabra_vocal[-1] in "aeiouAEIOU")


# #---------------------------------------------------------------------

# nombre= input("Ingrese su nombre: ")
# apellido= input("Ingrese su apellido: ")
# edad= input("Ingrese su edad: ")

# print(f"{nombre}-{apellido}-{edad}")
# #---------------------------------------------------------------------

# lista = [1,2,3,4,5,6,7,8]

# valor1= str(lista[0])
# valor2= str(lista[1])
# valor3= str(lista[2])
# valor4= str(lista[3])
# valor5= str(lista[4])

# print(valor1 + " " + valor2 + " " + valor3 + " " + valor4 + " " + valor5)


# ##segunda forma de hacerlo

# primeros_5 = lista[:5]
# print(" ".join(map(str, primeros_5)))

# #---------------------------------------------------------------------

# my_dicionary = {
#     "name": "liann",
#     "age": 24,
#     "course": "python",
# }

# print(my_dicionary)
# #---------------------------------------------------------------------

# ##join solo funciona con listas de string
# new_list=list(my_dicionary.keys())

# print("-".join(new_list))

# #---------------------------------------------------------------------

# ##añadir
# my_dicionary["course"]=["PHP","JAVA","C#"]
# my_dicionary["age"]=20
# my_dicionary["active"]=True

# ##cambiar el nombre a una llave
# if "course" in my_dicionary:
#     my_dicionary["courses"] = my_dicionary.pop("course")

# print(my_dicionary)

# #---------------------------------------------------------------------

list_numbers = [1,2,3,4,5,6,7,8,9,10]

for number in list_numbers:
    if number > 5 :
        print(f"{number} es mayor que 5")

sentence = "Hola mundo Curso de Python."
letras=0

for word in sentence.split():
    if "." in word:
        letras += len(word.split(".")[0])
        print (f"La palabra {word} tiene {len(word.split('.')[0])} letras")
        break
    else:
        letras += len(word)

# #---------------------------------------------------------------------
list =[(10,20),(30,40),(50,60),(70,80),(90,100)]

for i in list:
    print(f"{i[0]}-{i[1]}")