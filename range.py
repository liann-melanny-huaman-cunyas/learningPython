"""
for-each & while
"""
## range (start ,stop+1)
for number in range(10,21) :
    print(number)

number =[1,2,3,4,5,6]

for index in range(len(number)) : ## rangos enteros
    print(number[index])

cursos = ("java","php","python","javascript")

for curso in cursos :
    print(curso)


"""
While
"""

contador = 0

while contador < 10 :
    print('Valor:',contador)
    contador += 1