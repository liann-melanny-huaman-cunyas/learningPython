"""
Variable como Funciones
"""
def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):  # corregido nombre de función
    if amount > balance:
        return None
    return balance - amount

def default(*args, **kwargs):
    return '>>> Lo sentimos, opción no válida'

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
function = options.get(option, default)
total = function(balance, amount)

print(f"Resultado: {total}")
