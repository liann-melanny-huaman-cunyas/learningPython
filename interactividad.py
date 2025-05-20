nombre = input("dime tu nombre: ")
print(type(nombre))
print("Hola " + nombre )

edad = int(input("dime tu edad: "))
print(type(edad))
print("tienes " ,edad , " años")

estatura = float(input("¿Cuanto mides?: "))
print(type(estatura))
print("tienes " , estatura , " años")

redes = input("¿Tienes linkedin (yes /no)?: ")== "yes"
print(type(redes))
print( redes , "have linkedin")


name_dad,name_mom = "fredy", "marilu"

print("mi papá se llama " + name_dad + " y mi mamá se llama " + name_mom)
print("mi papá se llama {} y mi mamá se llama {}".format(name_dad, name_mom))