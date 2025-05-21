class ClaseZ:
    def say_hello(self):
        print(">>> Hola mundo, desde la clase Z!!!")

class ClaseA(ClaseZ):
    def say_hello(self):
        print(">>> Hola mundo, desde la clase A!!!")

class ClaseB:

    def say_hello(self):
        print(">>> Hola mundo, desde la clase B!!!")

    def say_goodbye(self):
        print(">>> Adios!")

class ClaseC(ClaseA, ClaseB):
    ...

c = ClaseC()
c.say_hello()
c.say_goodbye()