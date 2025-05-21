"""
Strings
Un string es una secuencia de caracteres, es inmutable,
lo que significa que no se puede cambiar una vez creado.
"""

message = "Hola Mundo"
print(message)
print(type(message))
print(message[0])

print("?!" in message)
print("Hola" in message)
print("Hola" not in message)

print(message.index("Mundo"))


message2 ="!"+ message[0:2] + " " + message[4:5] + " " + message[6:7]
print(message2)

"""
split :    separar un string en una lista de subcadenas
join :     unir una lista de subcadenas en un string
replace :  reemplazar una subcadena por otra
"""

mascotas = "afrodita cassie kanon butckus"
print(mascotas)

## resultado: ['afrodita cassie kanon butckus']
mascotas1= mascotas.split(",") ## cuando no hay ningun coma no se puede dividir
print(mascotas1)
## resultado: ['afrodita', 'cassie', 'kanon', 'butckus']
mascotas2= mascotas.split(" ") ## cuando haya un espacio se puede dividir
print(mascotas2)


lista_mascotas = ["hola", "mundo", "python"]
be="+".join(lista_mascotas)
print(be)
## resultado: "hola+mundo+python"


name = "liann"
last_name = "Huaman"

## primera forma de concatenar
full_name = name + " " + last_name
print(full_name)

## segunda forma de concatenar
full_name2 = f"{name} {last_name}"
print(full_name2)

## tercera forma de concatenar
full_name3 = "{} {}".format(name, last_name)
print(full_name3)

## cuarta forma de concatenar
full_name4 = ' '.join([name, last_name])
print(full_name4)

## quinta forma de concatenar
full_name5 = 'El nombre es: %s %s' % (name, last_name)
print(full_name5)


## sexta forma de concatenar format
bases = "El nombre es: {} {}"
print(bases.format(name, last_name))

"""
F-string | el recomendado
f"{variable1} {variable2}"
las variables deben estar definidas antes de usarlas pero tambien se pueden usar expresiones cambiantes
"""

name = "liann"
last_name = "Huaman"

full_name = f"El nombre es: {name} {last_name}"
print(full_name)


"""
Funcion print
"""

##separar con print
print("Hola", "Mundo", "Python", sep=", ")
print("Hola", "Mundo", "Python", sep=", ", end=".\n")