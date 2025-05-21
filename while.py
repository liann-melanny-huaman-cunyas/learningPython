import random
"""
WHILE
"""

# counter = 0
# number = int(input("Ingrese un número: "))


# while number >0 :
#     number = number//10
#     counter += 1
#     print("El número de dígitos es:", counter)


## ¿cuando se usa el while?
## Se usa cuando no sabemos cuantas veces se va a repetir el ciclo

## que numeor numero aleatoprio es

# numeor_adivinar = int(input("Ingrese un número entre 1 y 100: "))

# numero_aleatorio= random.randint(1,100)

# hits=0

# while numeor_adivinar != numero_aleatorio or hits>3 :
#     if numeor_adivinar < numero_aleatorio :
#         print("El número es mayor")
#     else :
#         print("El número es menor")
#     numeor_adivinar = int(input("Ingrese un número entre 1 y 100: "))


# print("El número aleatorio es:", numero_aleatorio)
# print("Felicidades, adivinaste el número")

## otro enunciado similae ejemplo
## 1. Escribir un programa que pida al usuario un número entero positivo y calcule la suma de todos los números
##    enteros desde 1 hasta ese número. El programa debe seguir pidiendo números hasta que el usuario ingrese un número negativo.

# numero_positivo = int(input("Ingrese un número entero positivo: "))
# suma = 0

# while numero_positivo >= 0 :
#     suma+= numero_positivo
#     numero_positivo = int(input("Ingrese un número entero positivo: "))
# print("La suma de los números es:", suma)


"""
break continue
"""
## break : termina el ciclo
## continue : salta a la siguiente iteración
## pass : no hace nada
## pass : se usa como un marcador de posición

## break
for number in range (8,21):
    if number%2 == 0:
        continue ##continua
    if number == 15:
        break ## termina
    print(number)
##pass or ...

for number in range (8,21):
    if number%2 == 0:
        pass ## no hace nada
    print(number)