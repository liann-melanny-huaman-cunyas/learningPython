"""
Funciones en python

def <nombre_funcion> (parametros):
    <cuerpo_funcion>
    return <valor_retorno>
"""
##Parametros opcionales

def sayhello():
    print("Hola mundo")

sayhello()


##itera 10 veces e imprime "Hola mundo"
for i in range(10):
    sayhello()


##Parametros obligatorios

def count(number):
    for i in range(number):
        print(i)

count(9)

def full_name(first_name, last_name):
    print(f"Hola {first_name} {last_name}")
    return full_name


## el return puede entrar por cada ciclo o def
def division(a,b):
    if(b==0 or a==0):
        return None
    return a/b

print(division(10,0))
print(division(10,5))



##retornar multiples valores
def full_name(first_name, last_name):
    return first_name, last_name ## crea una tupla

print(full_name("LIANN", "HUAMAN"))


def  mascota(name, age ,color):
    mascota=f'"{name} tiene {age} años y es de color {color}"'
    return mascota

print(mascota("Luna", 2, "blanco"))


## valores por defecto
def descuento(prenda,precio,descuento=0):
    precio_final=precio-(descuento*precio/100)
    if descuento > 0:
        return f"El precio de la {prenda} es {precio_final} con un descuento de {descuento}%"
    else:
        return f"El precio de la {prenda} es {precio_final} sin descuento"

print(descuento("camisa", 100, 20))
print(descuento("camisa", 100))


##Argumento
# * (posicion) - agrupa en un tupla
#** (nombre) - agrega en un diccionario

def suma(*args):
    suma=0
    for i in args:
        suma+=i
    return suma

suma(1,2,3,4,5)
suma(1,2,3,4,5,6,7,8,9,10)

def show_info(name,age,*gatos):
    print(f"Nombre: {name}")
    print(f"Edad: {age}")
    print("Gatos:")
    print("-".join(gatos))

show_info("Juan", 25, "afrodita","cassie","kanon")

##kwargs ¿Que es?

def show_info(**user):
    print(user)

show_info(
    username="Liann",
    correo ="lmelanny0604@gmail.com"
)

def show_inf2(*args,**kwargs):
    print(">>> Info")

    for value in args :
        print (value)
    # print("\n")
    print(">>>>> Details")
    for key , value in kwargs.items():
        print(key,value)


show_inf2(
    'Liann','Python',24,"liannmelanny@gmail.com",
    courses=["Python","Docker","React"],
    score=10
)