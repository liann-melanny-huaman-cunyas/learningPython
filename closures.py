"""
Closure

funciones anidades
"""

def  multiply(number1):
    def operation(number2):
        return number1*number2

    return operation


var1=10
func_operation=multiply(var1)


print("######### El resultado es ##########")
result=func_operation(3)
print(result)


"""
Decoradores
##funciona A(B)-> C
A DECORADOR
B FUNCION A DECORAR (BASE)
C (FUNCION DECORADA BASE + NUEVAS LINEAS DE CODIGO)
"""

def decorator(func):
    def wrapper(*args, **kwargs):
        print("antes del llamado")
        result = func(*args, **kwargs)
        print("despues del llamado")
        return result
    return wrapper

@decorator
def hello_world():
    print("hola mundo")

@decorator
def sumatoria(*args):
    suma = sum(args)
    print(suma)
    return suma

# Llamadas
hello_world()
resultado = sumatoria(20, 30, 50)
print("Resultado:", resultado)
