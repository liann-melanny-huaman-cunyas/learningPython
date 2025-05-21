"""
Lambda

lambda <parametro> : <body>
"""

##funcion lambda que suma dos numeros enteros

add=lambda number1,number2=0: number1+number2 ##return
print(add(10))
print(add(10,20))


abstrac=lambda *args:sum(args)
print(abstrac(1,2,3,4,5,6,7,8,9))

def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):  # corregido nombre de función
    if amount > balance:
        return None
    return balance - amount

#se elimina esta funcion por lamba de una linea
# def default(*args, **kwargs):
#     return '>>> Lo sentimos, opción no válida'

# Diccionario con opciones válidas
options = {
    'a': deposit,
    'b': withdraw
}

# Solicitar opción al usuario
option = input('Ingresa una opción (a: depositar / b: retirar): ').lower()
balance = int(input("Ingrese tu balance: "))
amount = int(input("Ingrese tu cantidad: "))

# Obtener función según la opción ingresada
function = options.get(option,
                       lambda *args ,**kwargs :'Lo sentimos opcion no valida')
total = function(balance, amount)

print(f"Resultado: {total}")
