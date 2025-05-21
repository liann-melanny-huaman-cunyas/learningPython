## match | 3.10

score = 10

match  score :
    case 10 :
        print("Tu calificacion es 10")
    case 9|8 :
        print("Aprobaste")

"""
Operador ternario
"""
message ='aprobaste' if score > 5 else "No aprobaste la materia"

print(message)