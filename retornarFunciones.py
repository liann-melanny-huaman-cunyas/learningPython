"""
Retornar Funciones
"""


##trabajar con fucniones de orden superior
##  Factory method

def factory_operation (option):
    def deposit(balance, amount=0):
        return balance + amount

    def withdraw(balance, amount=0):  # corregido nombre de función
        if amount > balance:
            return None

        return balance - amount

    default=lambda *args ,**kwargs :'Lo sentimos opcion no valida'

    if  option == 'deposit':
        return deposit
    elif option == "withdraw":
        return withdraw
    else:
        return default

option = input('Ingresa una opción (deposit / whitdraw): ').lower()
func = factory_operation(option)

print(func(100,20))
print(type(func))

