numbers = [ 1,2,3,4,5,6,7,8]

#sumar el primer y el ultimo elemento
print(numbers[0] + numbers[7])

#simar todos los elementos
print(numbers[1] + numbers[2]+ numbers[3] + numbers[4] + numbers[5] + numbers[6]+ numbers[7])

##una lista de longitud 10 de tipo string
strings_list=["ana","maria","jose","luis","pablo","carlos","javier","jorge","pedro","juan"]

#imprimir una nueva lista que tennga los 3 primeros y 3 ultimos elementos
new_list = strings_list[0:3] + strings_list[-3:]
##otra forma de hacerlo
new_list = strings_list[:3] + strings_list[-3:]
print(new_list)

##imprimir si codigo facilito esta en el list
print("CodigoFacilito" in strings_list)

##imprimir una matriz 3x3  e imprimir si el primer elemento de cada fila es un numero par
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    if row[0] % 2 == 0:
        print(f"El primer elemento de la fila {row} es par")
    else:
        print(f"El primer elemento de la fila {row} es impar")

##que es row
##row es una variable que representa cada fila de la matriz
##en cada iteracion del bucle for, row toma el valor de una fila de la matriz

##otra forma de hacerlo
for i in range(len(matrix)):
    if matrix[i][0] % 2 == 0:
        print(f"El primer elemento de la fila {i} {matrix[i][0]} es par")
    else:
        print(f"El primer elemento de la fila {i} {matrix[i][0]} es impar")