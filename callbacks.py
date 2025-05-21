"""
Callbacks
"""

## Recibir como argumentos otras funciones

def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):  # corregido nombre de función
    if amount > balance:
        return None
    return balance - amount

def handle_operation( callback ,*args ,**kwargs):
    print("#####proceso inciciado")
    result = callback(*args,**kwargs)
    print("El resultado es :",result)

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

handle_operation(
    callback=function,
    balance=balance,
    amount=amount
)