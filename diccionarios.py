"""
Diccionario
Este módulo contiene funciones para crear y manipular diccionarios en Python.
Un diccionario es una colección de pares clave-valor,
donde cada clave es única y se utiliza para acceder a su valor correspondiente.
Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación.
"""

user={
    "name": "liann",
    "age": 24,
    'isActive': True,
    "hobbies": ["programar", "leer", "correr"],
    "setings": (123,True),
}

print(user)
print ('name' in user) #True
print(user['name']) #liann
print(user.get('a', "la contraseña noexiste")) #liann

##no recomendable
user2={
    10 :"liann",
    20 :"Huaman",
    True:False
}


"""
METODOS DE LOS DICCIONARIOS
"""

##KEYS
## devuelve una lista de las claves del diccionario

##dict.keys()
print(user.keys()) #['name', 'age', 'isActive', 'hobbies', 'setings']

##list
print(list(user.keys())) #['name', 'age', 'isActive', 'hobbies', 'setings']

##tuple
print(tuple(user.keys())) #('name', 'age', 'isActive', 'hobbies', 'setings')

##VALUES
## devuelve una lista de los valores del diccionario

##dict.values()
print(user.values()) #['liann', 24, True, ['programar', 'leer', 'correr'], (123, True)]
##list
print(list(user.values())) #['liann', 24, True, ['programar', 'leer', 'correr'], (123, True)]
##tuple
print(tuple(user.values())) #('liann', 24, True, ['programar', 'leer', 'correr'], (123, True))

##ITEMS
## devuelve una lista de los pares clave-valor del diccionario
##dict.items()
print(user.items()) #dict_items([('name', 'liann'), ('age', 24), ('isActive', True), ('hobbies', ['programar', 'leer', 'correr']), ('setings', (123, True))])
##list
print(list(user.items())) #[('name', 'liann'), ('age', 24), ('isActive', True), ('hobbies', ['programar', 'leer', 'correr']), ('setings', (123, True))]
##tuple
print(tuple(user.items())) #(('name', 'liann'), ('age', 24), ('isActive', True), ('hobbies', ['programar', 'leer', 'correr']), ('setings', (123, True)))


"""
ACTUALIZAR DICCIONARIO
"""

mascota ={
    "id":1,
    "nombre":"afrodita",
    "raza":"persa",
    "edad":5,
    "hobbies":["comer", "dormir", "jugar"],
    "historial": {
        "vacunas": ["rabia", "parvovirus"],
        "visitas": ["veterinario", "peluqueria"]
    }
}

print(len(mascota)) #6

##remplazar
mascota["nombre"] = "kanon"

##añadir
mascota["lastname"] = "huaman"

mascota.update({
    "nombre":"kanon",
    "raza":"persa",
    "edad":5,
})

print(mascota)


cursos ={
    "curso1": {
        "nombre": "Python",
        "duracion": 3,
        "profesor": "Juan",
        "alumnos": ["Pedro", "Maria", "Jose"]
    },
    "curso2": {
        "nombre": "Java",
        "duracion": 4,
        "profesor": "Luis",
        "alumnos": ["Ana", "Juan", "Pedro"]
    },
    "curso3": {
        "nombre": "JavaScript",
        "duracion": 2,
        "profesor": "Maria",
        "alumnos": ["Jose", "Pedro", "Juan"]
    }
}
print(cursos)

del cursos["curso1"]["alumnos"][0] #eliminar el primer alumno
print(cursos)

##metodo pop
##ue hace el metodo pop?
##elimina el primer elemento de la lista y lo devuelve
##eliminar el primer alumno
alumno_eliminado = cursos["curso1"]["alumnos"].pop(0) #eliminar el primer alumno
print(alumno_eliminado) #Pedro
print(cursos)

alumnos = cursos.get("curso1", {}).get("alumnos", [])
alumnos.append("Liann")
print(alumnos)
