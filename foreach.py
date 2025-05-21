"""
Ciclo for each
"""

numbers = [1,2,3,4,5]

for i in numbers :
    print (i+1)

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

for key,value in cursos.items() :
    print("La llave es", key ,"y el valor", value)