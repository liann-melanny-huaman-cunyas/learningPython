"""
SCOPE
global -local
"""

username = 'liann' #global

def show_info():
    print(username)

show_info()


##funciones anidadas

def outer_function():
    message = "Holas desde adentro xd"

    def inner_function():
        nonlocal message ## ???
        message="info value"

    inner_function()
    print(message)


outer_function()